import os
import sys
def analyse_stats(directory, recursive):
    stats = {}
    for root,dirs,files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            extension = os.path.splitext(file)[1]
            file_size = os.path.getsize(filepath)
            if extension not in stats:
                stats[extension] = {'file_count': 0, 'largest_byte_size': 0, 'total_byte_size': 0}
            stats[extension]['file_count'] += 1
            if file_size > stats[extension]['largest_byte_size']:
                stats[extension]['largest_byte_size'] = file_size
            stats[extension]['total_byte_size'] += file_size
        if not recursive:
            break 
    return stats
def display_stats(stats):
    for extension, data in stats.items():
        print(f"{extension}\t{data['file_count']}\t{data['largest_byte_size']}\t{data['total_byte_size']}")
if __name__ == '__main__':
    directory = os.getcwd() 
    recursive = False
    for arg in sys.argv[1:]:
        if arg == '--r':
            recursive = True
        else:
            directory = arg 
    display_stats(analyse_stats(directory, recursive))
