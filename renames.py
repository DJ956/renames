import sys
import glob
import os

def main():
	argv = sys.argv
	if len(argv) != 4:
		print("Usage: python {} input(folder) ext(png, mp4)  \"del_str\"".format(argv[0]))
		quit(-1)

	src = argv[1]
	ext = argv[2]
	del_str = argv[3].replace("\"", "")

	files = glob.glob("{}/*.{}".format(src, ext))
	cnt = 1
	n = len(files)

	if n == 0:
		print("file not found.")
		quit(1)

	for file in files:
		befor = os.path.basename(file)
		after = befor.replace(del_str, '')
		out = "{}/{}".format(src, after)
		os.rename(file, out)
		print("[{}/{}]rename [{}] -> [{}]".format(cnt, n, befor, after))
		cnt += 1

	print("done.")

if __name__ == '__main__':
	main()