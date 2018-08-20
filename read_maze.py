import cv2

img = cv2.imread("maze.jpg",0)
img = cv2.resize(img, (495,495))
cv2.imshow("a",img)
cv2.waitKey(0)

N = 33
m = 15
print(m)

foo = open("maze.txt",'w')
threshold = 95
for i in range(33):
    for j in range(33):
        val = int(img[i*m:(i+1)*m, j*m:(j+1)*m].mean())
        print("{:3d}".format(val),end=' ')
        foo.write("{} ".format(1 if val>threshold else 0))
    print()
    foo.write("\n")
foo.close()
