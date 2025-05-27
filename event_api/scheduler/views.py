from rest_framework import generics, viewsets, permissions
from .serializers import RegisterSerializer, EventSerializer, BatchEventSerializer, EventPermissionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import User, Event
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from .models import EventPermission
from django.db.models import Q
from .permissions import IsEventOwnerOrEditorOrViewer
from rest_framework.exceptions import PermissionDenied


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsEventOwnerOrEditorOrViewer]

    def get_queryset(self):
        user = self.request.user
        owner_qs = Event.objects.filter(owner=user)
        shared_qs = Event.objects.filter(permissions__user=user)
        return (owner_qs | shared_qs).distinct()

    def get_object(self):
        queryset = Event.objects.all()
        obj = get_object_or_404(queryset, pk=self.kwargs["pk"])
        
        # Enforce object-level permission manually
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class BatchEventCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = BatchEventSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            events = serializer.save()
            return Response(EventSerializer(events, many=True).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ShareEventView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        event = get_object_or_404(Event, pk=id)

        # Only owner can share
        if event.owner != request.user:
            return Response({"detail": "Only the owner can share this event."}, status=status.HTTP_403_FORBIDDEN)

        data = request.data.get('users', [])
        shared = []

        for entry in data:
            user_id = entry.get('user_id')
            role = entry.get('role')

            if user_id == request.user.id:
                continue  # Prevent sharing with yourself

            user = get_object_or_404(User, pk=user_id)
            permission, created = EventPermission.objects.update_or_create(
                event=event,
                user=user,
                defaults={'role': role}
            )
            shared.append(EventPermissionSerializer(permission).data)

        return Response(shared, status=status.HTTP_200_OK)
    

