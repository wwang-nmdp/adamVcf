import argparse
def main():
    # parser = argparse.ArgumentParser(description='The seqAnn application')
    # parser.add_argument('-i', action="store", dest="vcf", help="The input vcf file")
    # parser.add_argument('-a', action="store", dest="adam", help="The inpu adam file")
    # options = parser.parse_args()
    # vcf = open(options.vcf, 'r')
    # adam = open(options.adam, 'r')
    vcf = open("/Users/wwang/Desktop/samples/vcfOut.csv", 'r')
    adam = open("/Users/wwang/Desktop/samples/adamOut.csv", 'r')
    rawline = "-1"
    while(rawline):
        rawline = vcf.readline()
        if rawline is not None:
            rawline = rawline.strip()
        else:
            break
        rawline = rawline[1:-1]
        line = adam.readline()
        if line != None:
            line = line.strip()
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
                while loop != len(rawData):
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
        print("True\n")
        vcf.close()
        adam.close()
        return True


if __name__ == '__main__':
    main()
