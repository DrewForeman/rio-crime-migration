import csv
import os


pre_2011_dir = '/Users/drewforeman/Documents/rioexp/opendirs_test/Pre2011'          #something is wrong in DO201009-look at csvs
pos_2011_dir = '/Users/drewforeman/Documents/rioexp/opendirs_test/Pos2011'

             

def extractmurders(file):                                           # The dataset is split up by reporting region, month and year,
                                                                    # meaning that I need to pull one specific data point from ~3,500
    with open(file) as f1:                                          # different csv files that do not have completely standard organization.
        alldata = csv.reader(f1)                                    # This function pulls the single data point from the given csv.
        alldata = list(alldata)

        if alldata[6][-5:]==['','','','','']:
            data_pt = alldata[6][-6]
        elif alldata[6][-1]=='':
            data_pt =  alldata[6][-2]
        else:
            data_pt =  alldata[6][-1]
    return float(data_pt)



def traverse_and_touch(directory, touch):                           # Inside the main directory there are subdirectories organized by 
    final_list = []                                                 # month and year. Inside each of those directories are 40 regional
                                                                    # data csvs. This function walks through each directory and touches
    for root, dirs, files in os.walk(directory):                    # each csv with an action "touch"
 
        new_list = [] 
                                                                               
        for filename in files:
            if filename!='.DS_Store' and filename!='Anexo-Table 1.csv' and filename!='Estadual-Table 1.csv' and filename!='Risp-Table 1.csv' \
            and filename!='RISP-Table 1.csv' and filename !='Errata-Table 1.csv' and filename!='ERRATA-Table 1.csv':
                value = touch(os.path.join(root, filename))
                new_list.append(value)                                                                                          
        # print new_list
        final_list.append(new_list)
    # print final_list
    return final_list



def reconfig_region_pos2011(jumbled_regions):                       # Rio's crime reporting regions were redistricted in 2011.
                                                                    # This function reconfigures the distribution of post-2011 regions
    jumbled_regions.remove([])                                      # so that they can be compared to pre-2011 data.
                                                                    # For info on how the districts changed and how I accounted for this 
    for item in jumbled_regions:                                    # change, see 'AispComparison.pd' file in ../. 
        item[2] = (item[2]+item[3]+item[4])/3
        item[7] = (item[7]+item[38])/2
        item[24] = (item[24]+item[37])/2
        item[25] = (item[25]+item[34])/2
        item[37] = item[36]

    for item in jumbled_regions:
        item[3] = 'x'
        item[4] = 'x'
        item[38] = 'x'
        item[36] = 'x'
        item[34] = 'x'
    
    for item in jumbled_regions:
        for i in item:
            if i == 'x':
                item.remove(i)

    for item in jumbled_regions:
        del item[-1]

    # print jumbled_regions
    return jumbled_regions
   


def reconfig_region_pre2011(jumbled_regions):                       # And this function reconfigures the pre-2011 regions for 
                                                                    # comparison with the reconfigured post-2011 data.
    jumbled_regions.remove([])

    for item in jumbled_regions:
        item[3] = (item[0]+item[3]+item[4]+item[5]+item[12])/5
        item[27] = (item[27]+item[36])/2
        item[26] = (item[26]+item[38])/2

    for item in jumbled_regions:
        item[0] = 'x'
        item[4] = 'x'
        item[5] = 'x'
        item[12] = 'x'
        item[36] = 'x'
        item[38] = 'x'
    
    for item in jumbled_regions:
        for i in item:
            if i == 'x':
                item.remove(i)

    for item in jumbled_regions:
        del item[-1]

    # print jumbled_regions
    return jumbled_regions



extracted_data_pre2011 = reconfig_region_pos2011(traverse_and_touch(pre_2011_dir, extractmurders))

extracted_data_pos2011 = reconfig_region_pos2011(traverse_and_touch(pos_2011_dir, extractmurders))


print extracted_data_pre2011
print extracted_data_pos2011


with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(extracted_data_pre2011)
    writer.writerows(extracted_data_pos2011)

