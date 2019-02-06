def cargar_Matriz(nombre_Archivo):
	return [[str(x) for x in y] for y in [x.split(" ") for x in [y.strip("\n") for y in open(nombre_Archivo).readlines()]]]

def obtener_n(nombre_Archivo):
	return len([c.strip("\n") for c in open(nombre_Archivo).readlines()])-1


def derecha(matriz,a,b,n):
	if b<=n:
		print matriz[a][b]
		derecha(matriz,a,b+1,n)
		

def abajo(matriz,a,b,n):
	if a<=n:
		print matriz[a][b]
		abajo(matriz,a+1,b,n)

def izquierda(matriz,a,b,n):
	if b>=0:
		print matriz[a][b]
		izquierda(matriz,a,b-1,n)

def arriba(matriz,a,b,n):
	if a>=1:	
		print matriz[a][b]
		arriba(matriz,a-1,b,n)

def caracol(matriz,a,b,n):
	if n==1:
		derecha(matriz,a,b,n)
		abajo(matriz,a+1,n,n)
		izquierda(matriz,n,n-1,n)
	elif n==2:
		derecha(matriz,a,b,n)
		abajo(matriz,a+1,n,n)
		izquierda(matriz,n,n-1,n)
		arriba(matriz,n-1,b,n)
		derecha(matriz,a+1,b+1,n-1)
	else:	
		derecha(matriz,a,b,n)
		abajo(matriz,a+1,n,n)
		izquierda(matriz,n,n-1,n)
		arriba(matriz,n-1,b,n)
		caracol(matriz,a+1,b+1,n-1)
			
def main(nombre_Archivo):
	try:
		caracol(cargar_Matriz(nombre_Archivo),0,0,obtener_n(nombre_Archivo))
	except Exception as e:
		print "Ocurrio un error "
	finally:
		print "Terminado"
	
main("matriz5x5.txt")