import os


home_dir = os.getcwd().
data_dir = os.path.join(home_dir, 'data')
src_dir = os.path.join(home_dir, 'src')
game_dir = os.path.join(home_dir, 'game')
list_dir = os.listdir(home_dir)

print(home_dir)
for (root, dirs, files) in os.walk(home_dir):
    print(root)
    print(dirs)
    print(files)
    print("-----")