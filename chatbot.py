import random

class MonkeyIslandAdventure:
    def __init__(self):
        self.start_story()

    def start_story(self):
        """Initialise ou redémarre le jeu."""
        print("\n🏴‍☠️ Arrr, bienvenue sur l'île aux singes ! Prêt pour une aventure légendaire, matelot ?")
        print("Le but : Trouver le trésor caché tout en évitant de finir jeté par-dessus bord. Choisis tes actions avec soin !\n")
        print("Tape 'recommencer' à tout moment pour redémarrer l'aventure, ou 'quitter' pour partir.")
        self.current_section = "start"
        self.game_over = False
        self.story_data = self.generate_story()
        self.run_game()

    def generate_story(self):
        """Structure l'histoire et les différentes branches."""
        return {
            "start": {
                "text": "Tu débarques sur une île mystérieuse. Par où veux-tu commencer ?",
                "options": {
                    "1": "Aller à la taverne pour trouver des infos.",
                    "2": "Explorer la jungle à la recherche du trésor.",
                    "3": "Interroger le capitaine d'un navire au port."
                },
                "next": {
                    "1": "taverne",
                    "2": "jungle_depart",
                    "3": "port"
                }
            },
            "taverne": {
                "text": "La taverne est pleine de pirates bruyants. Que fais-tu ?",
                "options": {
                    "1": "Commander un rhum pour discuter avec les pirates.",
                    "2": "Écouter discrètement les conversations.",
                    "3": "Défier un pirate à un duel d'insultes."
                },
                "next": {
                    "1": "indice_taverne",
                    "2": "indice_secret",
                    "3": "duel_taverne"
                }
            },
            "jungle_depart": {
                "text": "La jungle est dense et dangereuse. Après quelques pas, tu entends un bruit étrange. Que fais-tu ?",
                "options": {
                    "1": "Continuer vers le bruit.",
                    "2": "Rebrousser chemin vers la plage.",
                    "3": "Grimper à un arbre pour voir les alentours."
                },
                "next": {
                    "1": "singe_mysterieux",
                    "2": "start",
                    "3": "indice_arbre"
                }
            },
            "port": {
                "text": "Au port, tu trouves un vieux capitaine avec un perroquet. Il semble connaître des secrets. Que fais-tu ?",
                "options": {
                    "1": "Discuter avec lui pour des informations.",
                    "2": "Essayer de voler sa boussole.",
                    "3": "Lui proposer de t'emmener en mer."
                },
                "next": {
                    "1": "secret_capitaine",
                    "2": "attrape_vol",
                    "3": "embarque_navire"
                }
            },
            "indice_taverne": {
                "text": "Un pirate te confie que la carte du trésor est gardée par un singe au cœur de la jungle. Que fais-tu ?",
                "options": {
                    "1": "Partir immédiatement pour la jungle.",
                    "2": "Chercher un guide au port pour t'accompagner."
                },
                "next": {
                    "1": "jungle_depart",
                    "2": "port"
                }
            },
            "indice_arbre": {
                "text": "Depuis le sommet de l'arbre, tu vois une clairière avec une étrange lumière. Que fais-tu ?",
                "options": {
                    "1": "Descendre et aller vers la lumière.",
                    "2": "Rester en haut pour observer plus longtemps."
                },
                "next": {
                    "1": "singe_mysterieux",
                    "2": "jungle_depart"
                }
            },
            "singe_mysterieux": {
                "text": "Un singe apparaît avec une carte dans la main ! Que fais-tu ?",
                "options": {
                    "1": "Essayer de l'amadouer avec de la nourriture.",
                    "2": "Lui courir après pour prendre la carte."
                },
                "next": {
                    "1": "carte_obtenue",
                    "2": "singe_fache"
                }
            },
            "carte_obtenue": {
                "text": "Tu obtiens la carte ! Elle te conduit à un endroit précis dans la jungle. Que fais-tu ?",
                "options": {
                    "1": "Suivre la carte immédiatement.",
                    "2": "Retourner au port pour recruter un équipage."
                },
                "next": {
                    "1": "final_tresor",
                    "2": "port"
                }
            },
            "final_tresor": {
                "text": "Après une longue marche, tu trouves le trésor ! Félicitations ! Veux-tu rejouer ?",
                "options": {
                    "1": "Oui, recommençons l'aventure.",
                    "2": "Non, quitter le jeu."
                },
                "next": {
                    "1": "start",
                    "2": None
                }
            }
        }

    def run_game(self):
        """Boucle principale du jeu."""
        while not self.game_over:
            section = self.story_data[self.current_section]
            print("\nBarbossaBot : " + section["text"])
            
            # Si la section n'a pas d'options, terminer le jeu
            if "options" in section and section["options"]:
                for key, option in section["options"].items():
                    print(f"{key}. {option}")

                choice = input("Que fais-tu ? ").strip().lower()
                if choice == "recommencer":
                    self.start_story()
                    return
                elif choice == "quitter":
                    print("BarbossaBot : Bon vent, pirate ! À la prochaine aventure !")
                    self.game_over = True
                    return
                elif choice in section["next"]:
                    next_section = section["next"][choice]
                    if next_section:
                        self.current_section = next_section
                    else:
                        self.game_over = True
                        print("Merci d'avoir joué !")
                else:
                    print("Arrr ! Choix invalide, essaie encore !")
            else:
                print("Fin de l'aventure. Merci d'avoir joué !")
                self.game_over = True

# Lancer le jeu
if __name__ == "__main__":
    game = MonkeyIslandAdventure()
