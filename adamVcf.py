import argparse
def main():
    parser = argparse.ArgumentParser(description='Application for adam validation')
    parser.add_argument('-i', action="store", dest="vcf", help="The input vcf file")
    parser.add_argument('-a', action="store", dest="adam", help="The inpu adam file")
    options = parser.parse_args()
    # vcf = open(options.vcf, 'r')
    # adam = open(options.adam, 'r')
    vcf = open("/Users/wwang/Desktop/samples/1071904_vcfOut.csv", 'r')
    adam = open("/Users/wwang/Desktop/samples/1071904_adamOut.csv", 'r')
    rawline = "-1"
    while(rawline):
        rawline = vcf.readline()
        if rawline is not None:
            rawline = rawline.strip()
        else:
            break
        rawline = rawline[1:-1]
        line = adam.readline()
        backup = line
        line = line.strip()
        if line != None:
            line = adjustPosition(line)
        else:
            print(rawline + "\n")
            print(line + "\n")
            print("raw data not none, but adam is none\n")
            vcf.close()
            adam.close()
            return False

        if rawline == line:
            continue
        else:
            rawData = rawline.split(",")
            if len(rawData) == 4:
                print(rawline+"\n")
                print(line + "\n")
                print("raw data should contain more alts, False\n")
                vcf.close()
                adam.close()
                return False
            else:
                loop = 3
                while loop < len(rawData):
                    data = line.split(",")
                    if rawData[0] != data[0] or rawData[1] != data[1] or rawData[2] != data[2] or rawData[loop] != data[3]:
                        print(rawline + "\n")
                        print(line + "\n")
                        print("vcf not match adam,False\n")
                        vcf.close()
                        adam.close()
                        return False

                    else:
                       line = adam.readline()
                    loop += loop

    last = adam.readline()
    if(last):
        print(last + "\n")
        print("adam has more lines, False\n")
        vcf.close()
        adam.close()
        return False
    else:
        print(" Pass Validation! \n The ADAM file contains identical variants of the original VCF. \n")
        vcf.close()
        adam.close()
        return True


def isSame(vcf, adam):
    if vcf == adam:
        return True
    else:
        vcfData = vcf.split(",")
        adamData = adam.split(",")
        isPositionRight = int(vcfData[1]) == int(adamData[1]) - len(vcfData[3])
        if isPositionRight and vcfData[0] == adam[0] and vcfData[2] == adamData[2] and vcfData[3] == adamData[3]:
            return True
        else:
            return False


def adjustPosition(s):
    data = s.split(",")
    if len(data) < 4:

        return s

    data[1] = str(int(data[1]) - len(data[2]) + 1)
    return data[0]+","+data[1]+","+data[2]+","+data[3]

if __name__ == '__main__':
    main()
