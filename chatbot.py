def main():
    salir=0
    while salir !=1:
        EntradaMenu=int(input("Digite 1 para hacer preguntas sobre la especialidad\nDigite 2 para hacer preguntas sobre las subareas\nDigite 3 para salir del programa\n"))
        match EntradaMenu:
            case 1:
                esci=0
                while esci!=4:
                    EntradaMenuInter=int(input("Seleccione el tema del que desea hablar\n1-Que es?\n2-Que subareas abarca\n3-A que trabajos puedo aspirar\n4-Volver al menu principal\n"))
                    match EntradaMenuInter:
                        case 1:
                            print("Que es")
                        case 2:
                            print("Que subareas abarca")
                        case 3:
                            print("A que trabajo se puede aspirar")
                        case 4:
                            esci=4
            case 2:
                esci=0
                while esci!=1:
                    EntradaMenuInter=int(input("Seleccione la subarea de la que desea hablar\n1-Primera\n2-Segunda\n3-Tercera\n4-Cuarta\n5-Volver al menu\n"))
                    match EntradaMenuInter:
                        case 1:
                            sortir=0
                            while sortir!=1:
                                opc=int(input("Seleccione la opcion de la que desea hablar\n1-Que es\n2-Que temas abarca\n3-Que conocimiento concede\n4-Volver a las subareas\n5-Volver al menu principal\n"))
                                match opc:
                                    case 1:
                                        print("Que es")
                                    case 2:
                                        print("Que temas abarca")
                                    case 3:
                                        print("Que conocimineto concede")
                                    case 4:
                                        sortir=1
                                    case 5:
                                        sortir=1
                                        esci=1
                        case 2:
                            sortir=0
                            while sortir!=1:
                                opc=int(input("Seleccione la opcion de la que desea hablar\n1-Que es\n2-Que temas abarca\n3-Que conocimiento concede\n4-Volver a las subareas\n5-Volver al menu principal\n"))
                                match opc:
                                    case 1:
                                        print("Que es")
                                    case 2:
                                        print("Que temas abarca")
                                    case 3:
                                        print("Que conocimineto concede")
                                    case 4:
                                        sortir=1
                                    case 5:
                                        sortir=1
                                        esci=1
                        case 3:
                            sortir=0
                            while sortir!=1:
                                opc=int(input("Seleccione la opcion de la que desea hablar\n1-Que es\n2-Que temas abarca\n3-Que conocimiento concede\n4-Volver a las subareas\n5-Volver al menu principal\n"))
                                match opc:
                                    case 1:
                                        print("Que es")
                                    case 2:
                                        print("Que temas abarca")
                                    case 3:
                                        print("Que conocimineto concede")
                                    case 4:
                                        sortir=1
                                    case 5:
                                        sortir=1
                                        esci=1
                        case 4:
                            sortir=0
                            while sortir!=1:
                                opc=int(input("Seleccione la opcion de la que desea hablar\n1-Que es\n2-Que temas abarca\n3-Que conocimiento concede\n4-Volver a las subareas\n5-Volver al menu principal\n"))
                                match opc:
                                    case 1:
                                        print("Que es")
                                    case 2:
                                        print("Que temas abarca")
                                    case 3:
                                        print("Que conocimineto concede")
                                    case 4:
                                        sortir=1
                                    case 5:
                                        sortir=1
                                        esci=1
                        case 5:
                            esci=5
            case 3:
                salir=1
main()
#las variables esci y sortir funcionan igual que la variable salir, junto con el while funcionan como do while
#solo hay que cambiar las respuestas para que no repitan lo mismo que en la pregunta
