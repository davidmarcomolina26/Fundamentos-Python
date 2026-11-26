def draw_pattern(n):
    for row in range (n):
        for column in range(n):
            if row % 2 != 0:
                print('*', end=' ')
            else:
                print('-',end=' ')
        print()
#probador
print(draw_pattern(8))