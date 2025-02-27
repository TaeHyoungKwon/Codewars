"""
Informatycy to też ludzie, więc jak wszyscy potrzebują trochę miłości. Bajtek właśnie postanowił wyznać miłość pięknej Bajtolinie i w tym celu zamierza narysować jej N serduszek w ASCII art złożonych ze znaków małpy (@).

Jedno serduszko wygląda następująco:

 @@@   @@@ 
@   @ @   @
@    @    @
@         @
 @       @ 
  @     @  
   @   @   
    @ @    
     @     
Bajtek chciałby, żeby serduszka były wypisane jedno pod drugim. Pomóż mu!

Napisz program, który: wczyta liczbę N – liczbę serduszek, które Bajtek chce narysować Bajtolinie i wypisze na standardowe wyjście N serduszek w formacie opisanym powyżej.
"""

N = int(input())

for _ in range(N):
    print(" @@@   @@@ ")
    print("@   @ @   @")
    print("@    @    @")
    print("@         @")
    print(" @       @ ")
    print("  @     @  ")
    print("   @   @   ")
    print("    @ @    ")
    print("     @     ")
