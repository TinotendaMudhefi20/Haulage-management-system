from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

    def validate(self, data):
        truck = data.get('truck')
        driver = data.get('driver')

        #  Rule 1: Truck availability
        if truck.status in ['IN_TRANSIT', 'MAINTENANCE']:
            raise serializers.ValidationError("Truck is not available")

        # 👨 Rule 2: Driver active job check
        active_jobs = Job.objects.filter(
            driver=driver,
            status__in=['PENDING', 'IN_PROGRESS']
        )

        if active_jobs.exists():
            raise serializers.ValidationError("Driver already has an active job")

        return data

    def create(self, validated_data):
        job = super().create(validated_data)

        #  Update truck status when job starts
        if job.status == 'IN_PROGRESS':
            job.truck.status = 'IN_TRANSIT'
            job.truck.save()

        return job

    def update(self, instance, validated_data):
        new_status = validated_data.get('status', instance.status)

        job = super().update(instance, validated_data)

        # 🚛 Rule 3: Sync truck status
        if new_status == 'IN_PROGRESS':
            job.truck.status = 'IN_TRANSIT'
            job.truck.save()

        elif new_status == 'COMPLETED':
            job.truck.status = 'AVAILABLE'
            job.truck.save()

        return job