def main():
    salir=0
    while salir !=1:
        EntradaMenu=int(input("\n\n\n\nDigite 1 para hacer preguntas sobre la especialidad\nDigite 2 para hacer preguntas sobre las subareas\nDigite 3 para salir del programa\n"))
        match EntradaMenu:
            case 1:
                esci=0
                while esci!=4:
                    EntradaMenuInter=int(input("\n\n\n\nSeleccione el tema del que desea hablar\n1-Que es?\n2-Que subareas abarca\n3-A que trabajos puedo aspirar\n4-Volver al menu principal\n"))
                    match EntradaMenuInter:
                        case 1:
                            print("\n\n\n\nSe centra en la instalación, configuración, y mantenimiento de redes de comunicación y sistemas operativos. Los estudiantes adquieren habilidades \nen el diagnóstico de problemas, configuración de dispositivos de red, seguridad informática y administración de sistemas operativos.")
                        case 2:
                            print("\n\n\n\n1-Tecnologias aplicadas a la configuracion y soporte de redes y sistemas operativos\n2-Administracion y soporte a las computadoras\n3-Fundamentos de programacion\n4-Emprendimiento e innovacion\n5-Configuracion y soporte a redes\n6-Soporte TI")
                        case 3:
                            print("\n\n\n\nTécnico en redes\nAdministrador de sistemas\nSoporte técnico (TI)\nInstalador de redes\nEspecialista en seguridad de redes")
                        case 4:
                            esci=4
            case 2:
                esci=0
                while esci!=1:
                    EntradaMenuInter=int(input("\n\n\n\nSeleccione la subarea de la que desea hablar\n1-Tecnologias aplicadas a la configuracion y soporte de redes y sistemas operativos\n2-Administracion y soporte a las computadoras\n3-Fundamentos de programacion\n4-Emprendimiento e innovacion\n5-Configuracion y soporte a redes\n6-Soporte TI\n7-Volver al menu principal\n"))
                    match EntradaMenuInter:
                        case 1:
                            sortir=0
                            while sortir!=1:
                                opc=int(input("\n\n\n\nSeleccione la opcion de la que desea hablar\n1-Que es\n2-Que temas abarca\n3-Que conocimiento concede\n4-Volver a las subareas\n5-Volver al menu principal\n"))
                                match opc:
                                    case 1:
                                        print("\n\n\n\nSe enfoca en la instalación, configuración y mantenimiento de redes y sistemas operativos.")
                                    case 2:
                                        print("\n\n\n\nProtocolos de red, instalación de sistemas, resolución de problemas de conectividad.")
                                    case 3:
                                        print("\n\n\n\nComprensión de redes y sistemas operativos, y habilidades para asegurar su correcto funcionamiento.")
                                    case 4:
                                        sortir=1
                                    case 5:
                                        sortir=1
                                        esci=1
                        case 2:
                            sortir=0
                            while sortir!=1:
                                opc=int(input("\n\n\n\nSeleccione la opcion de la que desea hablar\n1-Que es\n2-Que temas abarca\n3-Que conocimiento concede\n4-Volver a las subareas\n5-Volver al menu principal\n"))
                                match opc:
                                    case 1:
                                        print("\n\n\n\nSe trata de gestionar y dar mantenimiento a computadoras, asegurando que funcionen de manera eficiente.")
                                    case 2:
                                        print("\n\n\n\nDiagnóstico y reparación de hardware y software, instalación de programas.")
                                    case 3:
                                        print("\n\n\n\nHabilidades técnicas para resolver problemas de equipos y mejorar su rendimiento.")
                                    case 4:
                                        sortir=1
                                    case 5:
                                        sortir=1
                                        esci=1
                        case 3:
                            sortir=0
                            while sortir!=1:
                                opc=int(input("\n\n\n\nSeleccione la opcion de la que desea hablar\n1-Que es\n2-Que temas abarca\n3-Que conocimiento concede\n4-Volver a las subareas\n5-Volver al menu principal\n"))
                                match opc:
                                    case 1:
                                        print("\n\n\n\nIntroducción a la lógica y los conceptos básicos para desarrollar programas informáticos.")
                                    case 2:
                                        print("\n\n\n\nEstructuras de control, variables, funciones.")
                                    case 3:
                                        print("\n\n\n\nCapacidad para entender y crear pequeños programas y aplicaciones.")
                                    case 4:
                                        sortir=1
                                    case 5:
                                        sortir=1
                                        esci=1
                        case 4:
                            sortir=0
                            while sortir!=1:
                                opc=int(input("\n\n\n\nSeleccione la opcion de la que desea hablar\n1-Que es\n2-Que temas abarca\n3-Que conocimiento concede\n4-Volver a las subareas\n5-Volver al menu principal\n"))
                                match opc:
                                    case 1:
                                        print("\n\n\n\nSe centra en fomentar el pensamiento creativo y el desarrollo de nuevas ideas empresariales.")
                                    case 2:
                                        print("\n\n\n\nInnovación, planes de negocio, liderazgo.")
                                    case 3:
                                        print("\n\n\n\nHabilidades para desarrollar y gestionar un negocio propio.")
                                    case 4:
                                        sortir=1
                                    case 5:
                                        sortir=1
                                        esci=1
                        case 5:
                            sortir=0
                            while sortir!=1:
                                opc=int(input("\n\n\n\nSeleccione la opcion de la que desea hablar\n1-Que es\n2-Que temas abarca\n3-Que conocimiento concede\n4-Volver a las subareas\n5-Volver al menu principal\n"))
                                match opc:
                                    case 1:
                                        print("\n\n\n\nAborda la creación y mantenimiento de redes informáticas.")
                                    case 2:
                                        print("\n\n\n\nCableado, configuración de routers y switches, seguridad de redes.")
                                    case 3:
                                        print("\n\n\n\nHabilidad para implementar y solucionar problemas en redes.")
                                    case 4:
                                        sortir=1
                                    case 5:
                                        sortir=1
                                        esci=1
                        case 6:
                            sortir=0
                            while sortir!=1:
                                opc=int(input("\n\n\n\nSeleccione la opcion de la que desea hablar\n1-Que es\n2-Que temas abarca\n3-Que conocimiento concede\n4-Volver a las subareas\n5-Volver al menu principal\n"))
                                match opc:
                                    case 1:
                                        print("\n\n\n\nBrinda soporte técnico a nivel de hardware y software dentro de una empresa.")
                                    case 2:
                                        print("\n\n\n\nSolución de problemas, soporte remoto, gestión de incidencias.")
                                    case 3:
                                        print("\n\n\n\nCapacidades para resolver problemas tecnológicos dentro de una organización.")
                                    case 4:
                                        sortir=1
                                    case 5:
                                        sortir=1
                                        esci=1
                        case 7:
                            esci=1
            case 3:
                salir=1
main()
#las variables esci y sortir funcionan igual que la variable salir, junto con el while funcionan como do while
#solo hay que cambiar las respuestas para que no repitan lo mismo que en la pregunta