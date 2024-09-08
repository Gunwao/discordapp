#!/bin/bash

# List of Docker image IDs to delete
image_ids=(
    "e1786d6d8b3e"
    "b3c68f859446"
    "e6195e799a5c"
    "614757ea0f4c"
    "036e1988451a"
    "ae5bc23f9c55"
    "4ec121465ff6"
    "942cb563f977"
    "4452d9ccead4"
    "c6258345918f"
    "43df367128b1"
    "baf8aab48cf7"
    "1fa6b85ba28f"
    "80837a474e71"
    "dbffb6da93b7"
    "8f45e1bb7a4c"
    "b559f5a6c8aa"
    "049a8e6cb3b4"
)

# Iterate through the list and delete each image
for image_id in "${image_ids[@]}"; do
    echo "Deleting Docker image: $image_id"
    docker rmi -f "$image_id"
done

echo "All specified Docker images have been deleted."