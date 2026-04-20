import os

files_to_update = ['dist/shop.html', 'dist/index.html']

replacements = {
    'class="flex gap-4 font-medium text-lg md:text-xl items-center"': 'class="flex flex-col md:flex-row gap-1 md:gap-4 font-medium text-lg md:text-xl items-start md:items-center"'
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
        
print("Price layout successfully made responsive in both shop.html and index.html")
