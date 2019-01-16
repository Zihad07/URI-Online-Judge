

def average_comment(average):
    if average<5.0:
        print("Aluno reprovado.")
    elif average<=6.9:
        print("Aluno em exame.")
    else:
        print("Aluno aprovado.")


def one_more_average_comment(new_average):
    
    if new_average<=4.9:
        print("Aluno reprovado.")
    elif new_average>=5:
        print("Aluno aprovado.")

a, b, c, d = map(float,input().split())




average = sum([a*2,b*3,c*4,d]) / 10

print("Media: %0.1f" %average)
average_comment(average)

if average>=5 and average<7:
    one_more = float(input())
    new_average = (average+float(one_more))/2.0
    print("Nota do exame:", float(one_more))
    one_more_average_comment(new_average)

    print("Media final: %0.1f" %new_average)

