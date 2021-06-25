import glob
import os

def main():
	files = glob.glob('../Validation Info/*/labels/*.txt')

	for file in files:

		fileName = file.split('\\')[-1]

		outFile = './mAP/input/detection-results/' + fileName

		dims = (1104, 800) # Image dimensions

		print('Converting file ' + fileName)

		readFile = open(file, 'r')
		writeFile = open(outFile, 'w')

		lines = readFile.read().split('\n')

		for line in lines:

			if len(line) != 0:

				# vector in the YOLOv5 format: class x_center y_center width height confidence
				v = line.split(' ')

				# Inputs in YOLOv5 format
				inClass = v[0]
				inXC = float(v[1])
				inYC = float(v[2])
				inW = float(v[3])
				inH = float(v[4])
				inConf = v[5]

				# Outputs in mAP format: <class_name> <confidence> <left> <top> <right> <bottom>

				XC = int(inXC*dims[0])
				YC = int(inYC*dims[1])

				semiW = int(inW*dims[0]/2)
				semiH = int(inH*dims[0]/2)

				left = str(XC - semiW)
				top = str(YC - semiH)
				right = str(XC + semiW)
				bottom = str(YC + semiH)

				outLine = inClass + ' ' + inConf + ' ' + left + ' ' + top + ' ' + right + ' ' + bottom + '\n'
				writeFile.write(outLine)

		readFile.close()
		writeFile.close()

if __name__ == '__main__':
	main()