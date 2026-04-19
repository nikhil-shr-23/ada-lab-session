# Input Modeling & Constraints for Delivery Routing

class DeliveryNetwork:
    def __init__(self):
        # 0 is the Warehouse. 1-4 are customer locations.
        self.locations = [0, 1, 2, 3, 4]
        
        # Distance matrix (Adjacency Matrix). Graph is fully connected.
        self.distance_matrix = [
            [0, 10, 15, 20, 25],
            [10, 0, 35, 25, 30],
            [15, 35, 0, 30, 20],
            [20, 25, 30, 0, 15],
            [25, 30, 20, 15, 0]
        ]
        
        # Parcel Metadata: {location: {'value': v, 'weight': w, 'time_window': (start, end)}}
        self.parcels = {
            1: {'value': 50, 'weight': 10, 'time_window': (0, 50)},
            2: {'value': 100, 'weight': 20, 'time_window': (10, 40)},
            3: {'value': 40, 'weight': 5, 'time_window': (20, 60)},
            4: {'value': 80, 'weight': 15, 'time_window': (30, 70)}
        }
        
        # Vehicle Configuration
        self.vehicle_capacity = 40
        self.speed = 1.0  # distance units per time unit

    def get_distance(self, from_node, to_node):
        return self.distance_matrix[from_node][to_node]

if __name__ == "__main__":
    net = DeliveryNetwork()
    print("Distance from 0 to 2:", net.get_distance(0, 2))
    print("Parcel at 2:", net.parcels[2])
