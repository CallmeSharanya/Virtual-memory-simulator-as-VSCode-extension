import psutil
import json

def format_size(bytes):
    """Convert bytes to a human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024

def get_memory_stats():
    """Fetch detailed memory statistics."""
    # Virtual Memory
    vm = psutil.virtual_memory()
    virtual_memory = {
        "Total Memory": format_size(vm.total),
        "Available Memory": format_size(vm.available),
        "Used Memory": format_size(vm.used),
        "Free Memory": format_size(vm.free),
        "Percentage Used": f"{vm.percent}%",
        # Add default/fallback for attributes not present in some systems
        "Buffers": format_size(getattr(vm, 'buffers', 0)),
        "Cached": format_size(getattr(vm, 'cached', 0)),
        "Active": format_size(getattr(vm, 'active', 0)),
        "Inactive": format_size(getattr(vm, 'inactive', 0)),
        "Shared Memory": format_size(getattr(vm, 'shared', 0)),
    }
    
    # Swap Memory
    swap = psutil.swap_memory()
    swap_memory = {
        "Total Swap": format_size(swap.total),
        "Used Swap": format_size(swap.used),
        "Free Swap": format_size(swap.free),
        "Percentage Swap Used": f"{swap.percent}%",
    }
    
    # Top Memory-Consuming Processes
    processes = sorted(psutil.process_iter(['pid', 'name', 'memory_info']), 
                       key=lambda p: p.info['memory_info'].rss if p.info['memory_info'] else 0, 
                       reverse=True)[:5]
    top_processes = [
        {
            "PID": p.info['pid'],
            "Name": p.info['name'],
            "Memory Used": format_size(p.info['memory_info'].rss) if p.info['memory_info'] else "N/A",
        }
        for p in processes
    ]
    
    # Combine all stats
    memory_stats = {
        "Virtual Memory": virtual_memory,
        "Swap Memory": swap_memory,
        "Top Memory Processes": top_processes,
    }
    
    return memory_stats

if __name__ == "__main__":
    memory_stats = get_memory_stats()
    print(json.dumps(memory_stats, indent=4))
