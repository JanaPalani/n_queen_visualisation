import pygame 
import time
pygame.init() 
plot = pygame.display.set_mode((400,400))

n = 8
queen_positions = []
all_block = {}
queen_num = 0
blocked_boxes = []
already_placed_position = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[]}
start = False

def block_box(pos):
    global all_block, blocked_boxes
    all_block[pos] = []

    for i in range(n):
        if board_value[(pos[0],i)] != '-' and board_value[(pos[0],i)] != 1:
            board_value[(pos[0],i)] = '-'
            all_block[pos].append((pos[0],i))   
        if board_value[(i,pos[1])] != '-' and board_value[(i,pos[1])] != 1:
            board_value[(i,pos[1])] = '-'
            all_block[pos].append((i,pos[1])) 
    for i in board_value.keys() :
        if pos[0]- pos[1] == i[0] - i[1] :
            if board_value[i] != '-' and board_value[i] != 1:
                board_value[i] = '-'
                all_block[pos].append(i) 

        if pos[0] + pos[1] == i[0] + i[1] :
            if board_value[i] != '-' and board_value[i] != 1:
                board_value[i] = '-'
                all_block[pos].append(i) 
    blocked_boxes.extend(all_block[pos])

        




def place_queen():
    global queen_num
    for i in range(n):
        if board_value[(queen_num,i)] == 0 :
            if (queen_num,i) not in already_placed_position[queen_num]:
                board_value[(len(queen_positions),i)] =  1
                already_placed_position[queen_num].append((queen_num,i))
                queen_positions.append((queen_num,i))
                block_box((queen_num,i))
                queen_num +=  1
                break
        else:
            continue
    else:
        back_track()

def back_track():
    global board_value , queen_positions , queen_num
    position = queen_positions[-1]
    board_value[position] = 0
    queen_positions = queen_positions[:-1]
    queen_num -= 1
    for i in all_block[position]:
        board_value[i] = 0
        blocked_boxes.remove(i)
    for i in range(queen_num +1,n):
        already_placed_position[i] = []





def board():
    board_value = {}
    for i in range(n):
        for j in range(n):
            board_value[(j, i)] = 0 
    return board_value

board_value = board()

run = True 
while run :

    plot.fill((250,250,250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = True
                
    
    if start :
        place_queen()
        time.sleep(0.1)

    if queen_num >= 8:
        start = False

            


     


    for i in queen_positions:
        pygame.draw.rect(plot,(0,200,200),(i[0]*50, i[1]*50, 50 , 50))
    
    for j in blocked_boxes:
        pygame.draw.rect(plot,(0,80,80),(j[0]*50, j[1]*50, 50 , 50))

    for i in board_value.keys():
        pygame.draw.rect(plot, (30,30,30) , (i[0]*50 , i[1]*50 , 50 , 50),2)

    pygame.display.flip()


