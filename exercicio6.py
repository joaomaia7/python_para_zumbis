distancia = int(input("Qual a distância a ser percorrida durante a viagem? ")) #pergunta a distância x de um determinada viagem;
velocidade_media = int(input("Aproximadamente, qual será a velocidade média durante o percurso? ")) #pergunta a velocidade media y deste mesmo percurso;

print(f'O tempo de duração da viagem será de {(distancia*velocidade_media)/3600:.2f} h') #imprime, em horas, o tempo de duração previsto para a viagem;
