import GPUtil
from tabulate import tabulate

def get_gpu_info():
    """Retrieve GPU information using GPUtil."""
    gpus = GPUtil.getGPUs()
    gpu_list = []

    for gpu in gpus:
        gpu_info = {
            "id": gpu.id,
            "name": gpu.name,
            "load": f"{gpu.load * 100:.1f}%",
            "free_memory": f"{gpu.memoryFree}MB",
            "used_memory": f"{gpu.memoryUsed}MB",
            "total_memory": f"{gpu.memoryTotal}MB",
            "temperature": f"{gpu.temperature}°C",
            "uuid": gpu.uuid,
        }
        gpu_list.append(gpu_info)

    return gpu_list


def print_gpu_info(gpu_list):
    """Print GPU information in a tabulated format."""
    headers = [
        "ID",
        "Name",
        "Load",
        "Free Memory",
        "Used Memory",
        "Total Memory",
        "Temperature",
        "UUID",
    ]
    table = [
        [
            gpu["id"],
            gpu["name"],
            gpu["load"],
            gpu["free_memory"],
            gpu["used_memory"],
            gpu["total_memory"],
            gpu["temperature"],
            gpu["uuid"],
        ]
        for gpu in gpu_list
    ]
    print(tabulate(table, headers=headers))


if __name__ == "__main__":
    gpu_list = get_gpu_info()
    print_gpu_info(gpu_list)
