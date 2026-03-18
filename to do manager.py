#All task are stored hear 
task=[]
#A loop which reapet all thing again and a gain 
while True:
    #ask what to do
    print("Press 1 To Add Task.")
    print("Press 2 To View Task.")
    print("Press 3 to Delete Task.")
    what_to_do= int(input("Press 4 To Exit.  "))
    #Decide what to do
    if (what_to_do==1):
        #Find how much task you have to add
        task_num=int(input("Tell How Much Task Did You Want To add.   "))
        task_runar=0
        #Add task one by one
        while (task_num>task_runar):
            task_runar+=1
            task_add=input(f"Enter Your {task_runar}rd Task.  ").lower()
            task.append(task_add)
    #Print task
    elif(what_to_do==2):
        print("This are the woke that you have to do, are:-")
        print("                                            ",", ".join(task))
    #Delete task 
    elif(what_to_do==3):
        #Which task to delete ask
        task_delete= input("Which task do you want to delete.").lower()
        #delete task
        for task_delete_num in task:
            if task_delete_num in task_delete:
                task.remove(task_delete_num)
        print("Your task is bing removed.")
        #to exit
    elif(what_to_do==4):
        print("Exit")
        break
    else:
        print("In valid option.")
        