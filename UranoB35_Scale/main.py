def uranob35_scale_converter():

    tag_data = {}
    tags = []

    demand_file = open('UranoB35_Scale\demandas.txt')
    demand_tags = demand_file.readlines()
        
    for tag in demand_tags:
        tag_data['tag_id'] = tag[55:62]
        tag_data['scale_id'] = tag[62:68]
        tag_data['weighing_date'] = tag[68:76]
        tag_data['weighing_hour'] = tag[76:84]
        tag_data['item_description'] = tag[96:123].strip()
        tag_data['item_id'] = tag[129:135]
        tag_data['item_weight'] = tag[139:145]

        tags.append(tag_data.copy())
        

    return tags

print(uranob35_scale_converter())



