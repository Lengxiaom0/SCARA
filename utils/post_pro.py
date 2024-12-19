

# target_postion: 目标物体的位置，0表示左边，1表示右边
# 识别的物体格式为：[x1,y1,x2,y2,postion_x,postion_y]

def post_pro(identified_objects_list,pred_list,first_bound,second_bound):
    if len(pred_list)<2:
        bound_center=[first_bound[0]+(first_bound[2]-first_bound[0])/2,first_bound[1]+(first_bound[3]-first_bound[1])/2]
    # 如果识别到的是第一个，那么就是0
    # 如果识别到的是第二个，那么就是1
    # 如果两个都不是，默认为第一个
    if pred_list[-1]==identified_objects_list[0]:
        bound_center=[first_bound[0]+(first_bound[2])//2,first_bound[1]+(first_bound[3])//2]
    elif pred_list[-1]==identified_objects_list[-1]:
        bound_center=[second_bound[0]+(second_bound[2])//2,second_bound[1]+(second_bound[3])//2]
    else:
        bound_center=[first_bound[0]+(first_bound[2])//2,first_bound[1]+(first_bound[3])//2]

    print("pred_list:",pred_list)
    if pred_list[0]=="左边" or pred_list[0]=="左侧" or pred_list[0]=="左上" or pred_list[0]=="左边上" or pred_list[0]=="左侧上":
        Target_postion_x=10
        Target_postion_y=300 
    elif pred_list[0]=="右边" or pred_list[0]=="右侧" or pred_list[0]=="右上" or pred_list[0]=="右边上" or pred_list[0]=="右侧上":
        Target_postion_x=600
        Target_postion_y=320 
    elif pred_list[0]=="中间" or pred_list[0]=="中心" or pred_list[0]=="中央":
        Target_postion_x=320
        Target_postion_y=320 
    elif pred_list[0]=="上边" or pred_list[0]=="顶部" or pred_list[0]=="上面" or pred_list[0]=="顶端":
        Target_postion_x=320
        Target_postion_y=10
    elif pred_list[0]=="下边" or pred_list[0]=="底部" or pred_list[0]=="下面" or pred_list[0]=="底端":
        Target_postion_x=320
        Target_postion_y=600 
    else:
        # 如果识别不到，默认左边
        Target_postion_x=100
        Target_postion_y=300 
    Target_postion=[Target_postion_x,Target_postion_y]

    return bound_center,Target_postion


    