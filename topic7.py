class Appointment:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

    def __repr__(self):
        return f"{self.description} (Priority: {self.priority})"


class BucketSort:
    def __init__(self, appointments):
        self.appointments = appointments

    def bucket_sort(self):
        # Determine the range of priorities
        max_priority = max(appointment.priority for appointment in self.appointments)
        min_priority = min(appointment.priority for appointment in self.appointments)

        # Create buckets for each priority level
        bucket_range = max_priority - min_priority + 1
        buckets = [[] for _ in range(bucket_range)]

        # Distribute the appointments into their respective buckets based on priority
        for appointment in self.appointments:
            bucket_index = appointment.priority - min_priority
            buckets[bucket_index].append(appointment)

        # Sort each bucket individually and combine them
        sorted_appointments = []
        for bucket in buckets:
            sorted_appointments.extend(sorted(bucket, key=lambda x: x.priority))

        return sorted_appointments


# Example usage:

# Creating a list of appointments with descriptions and priorities
appointments = [
    Appointment("Haircut at 10:00 AM", 3),
    Appointment("Facial at 11:00 AM", 1),
    Appointment("Massage at 2:00 PM", 2),
    Appointment("Haircut at 3:00 PM", 2),
    Appointment("Facial at 4:00 PM", 1)
]

# Display original list of appointments
print("Original list of appointments:")
for appointment in appointments:
    print(appointment)

# Create an instance of BucketSort and sort the appointments
bucket_sorter = BucketSort(appointments)
sorted_appointments = bucket_sorter.bucket_sort()

# Display sorted appointments
print("\nSorted list of appointments based on priority:")
for appointment in sorted_appointments:
    print(appointment)


