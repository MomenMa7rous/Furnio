import os

files_to_update = ['dist/shop.html', 'dist/index.html']

replacements = {
    'class="text-xl text-title font-semibold"': 'class="text-xl md:text-2xl text-title font-semibold"',
    'class="text-par font-medium text-xs"': 'class="text-par font-medium text-xs md:text-sm"',
    'class="flex gap-4 font-medium text-lg items-center"': 'class="flex gap-4 font-medium text-lg md:text-xl items-center"',
    'class="text-par/80 line-through text-xs font-normal"': 'class="text-par/80 line-through text-xs md:text-sm font-normal"'
}

for filepath in files_to_update:
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old_str, new_str in replacements.items():
        content = content.replace(old_str, new_str)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Text sizes successfully made responsive in both shop.html and index.html")
