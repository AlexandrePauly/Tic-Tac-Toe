#!/usr/bin/env python3
"""! @brief Programme Python pour jouer au jeu du Morpion."""
##
# @mainpage project.py
#
# @section Description
# Ensemble des fonctions du projet.
#
##
# @file interface.py
#
# @brief Interface pour effectuer la reconnaissance d'une empreinte digitale
#
# @section Description
# Interface Python réalisée avec la libraire Tkinter.
#
# @section Libraries/Modules
# - tkinter extern library (https://docs.python.org/fr/3/library/tkinter.html)
# - random standard library (https://docs.python.org/fr/3/library/random.html?highlight=random#module-random)
# - time standard library (https://docs.python.org/fr/3/library/time.html)
#
# @section Auteur
# - PAULY Alexandre
##

# Import des bibliothèques nécessaires
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, font
import random
import time

def checkRow(token):
    """! Recherche de vainqueur sur les lignes

    Fonction pour vérifier si la partie est gagnée en ligne.

    @param token: Pion du joueur
    @type token: String

    @return: Vrai ou Faux
    @rtype: Boolean

    """

    if(game_button1.cget("text") == game_button2.cget("text") == game_button3.cget("text") == token):
        return True
    elif(game_button4.cget("text") == game_button5.cget("text") == game_button6.cget("text") == token):
        return True
    elif(game_button7.cget("text") == game_button8.cget("text") == game_button9.cget("text") == token):
        return True
    else: 
        return False

def checkColumn(pion):
    """! Recherche de vainqueur sur les colonnes

    Fonction pour vérifier si la partie est gagnée en colonne.

    @param token: Pion du joueur
    @type token: String

    @return: Vrai ou Faux
    @rtype: Boolean

    """

    if(game_button1.cget("text") == game_button4.cget("text") == game_button7.cget("text") == pion):
        return True
    elif(game_button2.cget("text") == game_button5.cget("text") == game_button8.cget("text") == pion):
        return True
    elif(game_button3.cget("text") == game_button6.cget("text") == game_button9.cget("text") == pion):
        return True
    else: 
        return False

def checkDiag(pion):
    """! Recherche de vainqueur sur les diagonales

    Fonction pour vérifier si la partie est gagnée en diagonale.

    @param token: Pion du joueur
    @type token: String

    @return: Vrai ou Faux
    @rtype: Boolean

    """

    if(game_button1.cget("text") == game_button5.cget("text") == game_button9.cget("text") == pion):
        return True
    elif(game_button3.cget("text") == game_button5.cget("text") == game_button7.cget("text") == pion):
        return True
    else: 
        return False

def checkWin(pion):
    """! Recherche d'un vainqueur

    Fonction pour vérifier si la partie est gagnée.

    @param token: Pion du joueur
    @type token: String

    @return: Vrai ou Faux
    @rtype: Boolean

    """

    if (checkRow(pion) or checkColumn(pion) or checkDiag(pion)):
        return True

    return False

def on_select_token(event):
    """! Changement de pion

    Fonction pour changer le pion du joueur.

    @param event: Pion du joueur
    @type event: String

    """

    # Déclaration de variables globales pour stocker les valeurs des pions des joueurs
    global token_player, token_AI

    # Initialisation de variables
    selected_item = combobox1.get() # Valeur de la combobox
    token_player = selected_item     # Attribution au pion

    # Inversement des pions du joueur et de l'IA
    if token_player == "X":
        token_AI = "O"
    else:
        token_AI = "X" 

def on_select_difficulty(event):
    """! Changement de difficulté

    Fonction pour changer la difficulté de l'IA.

    @param event: Difficulté de l'IA
    @type event: String

    """

    # Déclaration de variables globales pour stocker la difficulté de l'IA
    global difficulty

    # Initialisation de variables
    selected_item = combobox2.get() # Valeur de la combobox
    difficulty = selected_item      # Attribution au pion
        
def on_change_filter(elt):
    """! Changement de thème de couleur

    Fonction pour changer le thème de couleur de l'interface.

    @param elt: Thème de couleur
    @type elt: elt

    """

    if (elt == "Basic"):
        # Définition des styles
        background_color = "lightgrey"
        border_color = "black"
        title_color = "black"
        buttonActivated_color = "grey"
        button_color = "lightgrey"
        tictactoeBorder_color = "black"
        tictactoeButton_color = "lightgrey"
        startButton_color = "lightgrey"

        # Application de styles sur les boutons
        filter_button1.config(state="disabled", cursor="arrow")
        filter_button2.config(state="normal", cursor="hand2")
        filter_button3.config(state="normal", cursor="hand2")
        filter_button4.config(state="normal", cursor="hand2")
        filter_button1.configure(bg=buttonActivated_color)
        filter_button2.configure(bg=button_color)
        filter_button3.configure(bg=button_color)
        filter_button4.configure(bg=button_color)
    elif (elt == "Original"):
        # Définition des styles
        background_color = "#e5e5dc"
        border_color = "#c4a35a"
        title_color = "#c4a35a"
        buttonActivated_color = "#c66b3d"
        button_color = "#e5e5dc"
        tictactoeBorder_color = "#042940"
        tictactoeButton_color = "lightgrey"
        startButton_color = "#c66b3d"

        # Application de styles sur les boutons
        filter_button1.config(state="normal", cursor="hand2")
        filter_button2.config(state="disabled", cursor="arrow")
        filter_button3.config(state="normal", cursor="hand2")
        filter_button4.config(state="normal", cursor="hand2")
        filter_button1.configure(bg=button_color)
        filter_button2.configure(bg=buttonActivated_color)
        filter_button3.configure(bg=button_color)
        filter_button4.configure(bg=button_color)
    elif(elt == "Light"):
        # Définition des styles
        background_color = "#ccccb2"
        border_color = "#005C53"
        title_color = "white"
        buttonActivated_color = "#D6D58E"
        button_color = "#9FC131"
        tictactoeBorder_color = "#005C53"
        tictactoeButton_color = "#D6D58E"
        startButton_color = "#D6D58E"

        # Application de styles sur les boutons
        filter_button1.config(state="normal", cursor="hand2")
        filter_button2.config(state="normal", cursor="hand2")
        filter_button3.config(state="disabled", cursor="arrow")
        filter_button4.config(state="normal", cursor="hand2")
        filter_button1.configure(bg=button_color)
        filter_button2.configure(bg=button_color)
        filter_button3.configure(bg=buttonActivated_color)
        filter_button4.configure(bg=button_color)
    else:
        # Définition des styles
        background_color = "#11131e"
        border_color = "#f9f9f9"
        title_color = "#f9f9f9"
        buttonActivated_color = "#5372F0"
        button_color = "#6C757D"
        tictactoeBorder_color = "#11131e"
        tictactoeButton_color = "lightgrey"
        startButton_color = "#5372F0"

        # Application de styles sur les boutons
        filter_button1.config(state="normal", cursor="hand2")
        filter_button2.config(state="normal", cursor="hand2")
        filter_button3.config(state="normal", cursor="hand2")
        filter_button4.config(state="disabled", cursor="arrow")
        filter_button1.configure(bg=button_color)
        filter_button2.configure(bg=button_color)
        filter_button3.configure(bg=button_color)
        filter_button4.configure(bg=buttonActivated_color)

    # Application de styles
    leftCol_content.configure(bg=background_color)
    leftCol_subcontent.configure(bg=background_color)
    leftCol_border.configure(bg=border_color)
    filter_label.configure(bg=background_color, foreground=title_color)
    filter_frame.configure(bg=background_color)
    container.configure(bg=background_color)
    subcontainer1.configure(bg=background_color)
    subcontainer2.configure(bg=background_color)
    label1.configure(bg=background_color, foreground=title_color)
    label2.configure(bg=background_color, foreground=title_color)
    game_history_label.configure(bg=background_color, foreground=title_color)
    win1_label.configure(bg=background_color, foreground=title_color)
    win2_label.configure(bg=background_color, foreground=title_color)
    equality_label.configure(bg=background_color, foreground=title_color)
    rightCol_content.configure(bg=background_color)
    game_frame.configure(bg=tictactoeBorder_color)
    manageGame_frame.configure(bg=background_color)
    button_reset.configure(bg=button_color)
    button_start.configure(bg=startButton_color)
    game_button1.configure(bg=tictactoeButton_color)
    game_button2.configure(bg=tictactoeButton_color)
    game_button3.configure(bg=tictactoeButton_color)
    game_button4.configure(bg=tictactoeButton_color)
    game_button5.configure(bg=tictactoeButton_color)
    game_button6.configure(bg=tictactoeButton_color)
    game_button7.configure(bg=tictactoeButton_color)
    game_button8.configure(bg=tictactoeButton_color)
    game_button9.configure(bg=tictactoeButton_color)

    if(elt == "Original"):
        # Définition des styles
        mainColor = "#042940"

        # Application de styles
        leftCol_subcontent.configure(bg=mainColor)
        filter_label.configure(bg=mainColor, foreground=title_color)
        filter_frame.configure(bg=mainColor)
        container.configure(bg=mainColor)
        subcontainer1.configure(bg=mainColor)
        subcontainer2.configure(bg=mainColor)
        label1.configure(bg=mainColor, foreground=title_color)
        label2.configure(bg=mainColor, foreground=title_color)
        game_history_label.configure(bg=mainColor, foreground=title_color)
        win1_label.configure(bg=mainColor, foreground=title_color)
        win2_label.configure(bg=mainColor, foreground=title_color)
        equality_label.configure(bg=mainColor, foreground=title_color)
    elif(elt == "Light"):
        # Définition des styles
        mainColor = "#005C53"

        # Application de styles
        leftCol_subcontent.configure(bg=mainColor)
        filter_label.configure(bg=mainColor, foreground=title_color)
        filter_frame.configure(bg=mainColor)
        container.configure(bg=mainColor)
        subcontainer1.configure(bg=mainColor)
        subcontainer2.configure(bg=mainColor)
        label1.configure(bg=mainColor, foreground=title_color)
        label2.configure(bg=mainColor, foreground=title_color)
        game_history_label.configure(bg=mainColor, foreground=title_color)
        win1_label.configure(bg=mainColor, foreground=title_color)
        win2_label.configure(bg=mainColor, foreground=title_color)
        equality_label.configure(bg=mainColor, foreground=title_color)

def switchPlayer():
    """! Changement de joueur 

    Fonction pour changer le joueur qui commence la partie (joueur ou IA).

    """

    global first_player

    if first_player == "AI":
        first_player = "player"
    else:
        first_player = "AI" 

def bestMove():
    """! Recherche du meilleur coup à jouer

    Fonction pour calculer le meilleur coup à jouer pour l'IA. Par défaut, l'algorithme recherche une victoire, mais va tout de même chercher à bloquer le joueur en cas de possibilité de victoire imminente.

    Étapes de l'algorithme :
        - Dans un premier temps, l'algo vérifie si certaines combinaisons ne sont pas impératives, c'est-à-dire si l'IA ou le joueur ne peuvent pas gagner dans un premier coup. Pour ce faire il va jouer la case en question pour gagner ou bloquer la victoire au joueur.
        - Si l'algo n'a pas trouvé de possibilité précédemment, il va parcourir l'ensemble des cases pour calculer la meilleure case à jouer en incrémentant un indice en fonction du nombre de ses pions présents sur les lignes, colonnes et diagonales de chaque case.
        - Après cette étape, il va récupérer la case avec l'indice le plus élevé afin de rechercher une victoire. 

    @return: La valeur de la case à jouer
    @rtype: Number

    """

    global difficulty

    # Retourne la case à jouer lorsqu'il est possible de gagner directement ou de bloquer une victoire imminente du joueur
    if difficulty == "Hard" and game_button1.cget("text") == "" and ((game_button2.cget("text") == game_button3.cget("text") == token_AI) or (game_button4.cget("text") == game_button7.cget("text") == token_AI) or (game_button5.cget("text") == game_button9.cget("text") == token_AI)):
        return 1 
    elif difficulty == "Hard" and game_button2.cget("text") == "" and ((game_button1.cget("text") == game_button3.cget("text") == token_AI) or (game_button5.cget("text") == game_button8.cget("text") == token_AI)):
        return 2 
    elif difficulty == "Hard" and game_button3.cget("text") == "" and ((game_button1.cget("text") == game_button2.cget("text") == token_AI) or (game_button6.cget("text") == game_button9.cget("text") == token_AI) or (game_button5.cget("text") == game_button7.cget("text") == token_AI)):
        return 3 
    elif difficulty == "Hard" and game_button4.cget("text") == "" and ((game_button1.cget("text") == game_button7.cget("text") == token_AI) or (game_button5.cget("text") == game_button6.cget("text") == token_AI)):
        return 4 
    elif difficulty == "Hard" and game_button5.cget("text") == "" and ((game_button1.cget("text") == game_button9.cget("text") == token_AI) or (game_button3.cget("text") == game_button7.cget("text") == token_AI) or (game_button2.cget("text") == game_button8.cget("text") == token_AI) or (game_button4.cget("text") == game_button6.cget("text") == token_AI)):
        return 5 
    elif difficulty == "Hard" and game_button6.cget("text") == "" and ((game_button3.cget("text") == game_button9.cget("text") == token_AI) or (game_button4.cget("text") == game_button5.cget("text") == token_AI)):
        return 6 
    elif difficulty == "Hard" and game_button7.cget("text") == "" and ((game_button1.cget("text") == game_button4.cget("text") == token_AI) or (game_button8.cget("text") == game_button9.cget("text") == token_AI) or (game_button3.cget("text") == game_button5.cget("text") == token_AI)):
        return 7 
    elif difficulty == "Hard" and game_button8.cget("text") == "" and ((game_button2.cget("text") == game_button5.cget("text") == token_AI) or (game_button7.cget("text") == game_button9.cget("text") == token_AI)):
        return 8 
    elif difficulty == "Hard" and game_button9.cget("text") == "" and ((game_button3.cget("text") == game_button6.cget("text") == token_AI) or (game_button7.cget("text") == game_button8.cget("text") == token_AI) or (game_button1.cget("text") == game_button5.cget("text") == token_AI)):
        return 9
    elif difficulty == "Hard" and game_button1.cget("text") == "" and ((game_button2.cget("text") == game_button3.cget("text") == token_player) or (game_button4.cget("text") == game_button7.cget("text") == token_player) or (game_button5.cget("text") == game_button9.cget("text") == token_player)):
        return 1 
    elif difficulty == "Hard" and game_button2.cget("text") == "" and ((game_button1.cget("text") == game_button3.cget("text") == token_player) or (game_button5.cget("text") == game_button8.cget("text") == token_player)):
        return 2 
    elif difficulty == "Hard" and game_button3.cget("text") == "" and ((game_button1.cget("text") == game_button2.cget("text") == token_player) or (game_button6.cget("text") == game_button9.cget("text") == token_player) or (game_button5.cget("text") == game_button7.cget("text") == token_player)):
        return 3 
    elif difficulty == "Hard" and game_button4.cget("text") == "" and ((game_button1.cget("text") == game_button7.cget("text") == token_player) or (game_button5.cget("text") == game_button6.cget("text") == token_player)):
        return 4
    elif difficulty == "Hard" and game_button5.cget("text") == "" and ((game_button1.cget("text") == game_button9.cget("text") == token_player) or (game_button3.cget("text") == game_button7.cget("text") == token_player) or (game_button2.cget("text") == game_button8.cget("text") == token_player) or (game_button4.cget("text") == game_button6.cget("text") == token_player)):
        return 5 
    elif difficulty == "Hard" and game_button6.cget("text") == "" and ((game_button3.cget("text") == game_button9.cget("text") == token_player) or (game_button4.cget("text") == game_button5.cget("text") == token_player)):
        return 6 
    elif difficulty == "Hard" and game_button7.cget("text") == "" and ((game_button1.cget("text") == game_button4.cget("text") == token_player) or (game_button8.cget("text") == game_button9.cget("text") == token_player) or (game_button3.cget("text") == game_button5.cget("text") == token_player)):
        return 7 
    elif difficulty == "Hard" and game_button8.cget("text") == "" and ((game_button2.cget("text") == game_button5.cget("text") == token_player) or (game_button7.cget("text") == game_button9.cget("text") == token_player)):
        return 8 
    elif difficulty == "Hard" and game_button9.cget("text") == "" and ((game_button3.cget("text") == game_button6.cget("text") == token_player) or (game_button7.cget("text") == game_button8.cget("text") == token_player) or (game_button1.cget("text") == game_button5.cget("text") == token_player)):
        return 9
    # Sinon recherche du meilleur coup en fonction du plateau de jeu
    else:
        # Initialisation de variables
        l = 0                                                     # Variable de boucle
        k = 0                                                     # Variable de boucle
        tabMove = [0] * 9                                         # Tableau de la valeur de chaque coup possible
        bestMove = -1                                             # Meilleur coup à jouer
        positionMove = -1                                         # Position du meilleur coup à jouer
        game_buttons = [game_button1, game_button2, game_button3, 
                        game_button4, game_button5, game_button6, 
                        game_button7, game_button8, game_button9] # Liste des boutons de jeu au morpion
        rows = [
            [game_buttons[0], game_buttons[1], game_buttons[2]],  # Première ligne
            [game_buttons[3], game_buttons[4], game_buttons[5]],  # Deuxième ligne
            [game_buttons[6], game_buttons[7], game_buttons[8]]   # Troisième ligne
        ]                                                         # Tableau des lignes

        columns = [
            [game_buttons[0], game_buttons[3], game_buttons[6]],  # Première colonne
            [game_buttons[1], game_buttons[4], game_buttons[7]],  # Deuxième colonne
            [game_buttons[2], game_buttons[5], game_buttons[8]]   # Troisième colonne
        ]                                                         # Tableau des colonnes

        diagonals = [
            [game_buttons[0], game_buttons[4], game_buttons[8]],  # Première diagonale
            [game_buttons[2], game_buttons[4], game_buttons[6]]   # Deuxième diagonale
        ]                                                         # Tableau des diagonales

        # Pour chaque élément de game_buttons, on récupère le texte du bouton pour modifier les colonnes du tableau
        for button in game_buttons:
            # Remplacement du texte
            game_buttons[l] = button.cget("text")

            # Incrémentation d'un indice de boucle
            l += 1

        # Parcours de toutes les cases. Elles sont incrémentées en fonction des pions jouées autour de ces dernières. +1 lorsqu'un pion de l'IA est placé sur la même ligne, collonne ou diagonale
        # Pour toutes les lignes
        for i in range(3):
            # Initialisation de variables
            check = False # Booléen pour effectuer une action qu'une seule fois

            # Pour toutes les colonnes
            for j in range(3):
                if not check:
                    tabMove[k] += sum(1 for button in rows[i] if button == token_AI)
                    check = True

                tabMove[k] += sum(1 for button in columns[j] if button == token_AI)

                # Si c'est la première ligne
                if i == 0:
                    # Si c'est la première colonne
                    if j == 0:
                        tabMove[0] += sum(1 for button in diagonals[0] if button == token_AI)
                    # Sinon, si c'est la dernière colonne
                    elif j == 2:
                        tabMove[2] += sum(1 for button in diagonals[1] if button == token_AI)
                # Sinon, si c'est la deuxième ligne et deuxième colonne
                elif i == 1 and j == 1:
                    tabMove[4] += sum(1 for button in diagonals[1] if button == token_AI)
                # Sinon, si c'est la dernière ligne
                elif i == 2:
                    # Si c'est la première colonne
                    if j == 0:
                        tabMove[8] += sum(1 for button in diagonals[0] if button == token_AI)
                    # Sinon, si c'est la dernière colonne
                    elif j == 2:
                        tabMove[6] += sum(1 for button in diagonals[1] if button == token_AI)

                # Incrémentation d'une variable de boucle
                k += 1

        # Pour chaque élément de tabMove
        for i in range(len(tabMove)):
            # Si la valeur de l'élément est supérieure à celle de l'actuel meilleur coup, il devient le meilleur coup
            if (tabMove[i] > bestMove and game_buttons[i] == ""):
                bestMove = tabMove[i] # Mise à jour du meilleur coup
                positionMove = i      # Mise à jour de la position du meilleur coup

        # Retourne le meilleur coup à jouer
        return (positionMove + 1)

def AI_play():
    """! Tour de jeu de l'IA

    Fonction pour faire jouer l'IA. Joue sur la case centrale en priorité si elle n'a pas été jouée, sinon calcule la case la plus importante à jouer à l'aide de la fonction bestMove.

    """

    # Initialisation de variables
    game_buttons = [game_button1, game_button2, game_button3, game_button4, game_button5, game_button6, game_button7, game_button8, game_button9] # Liste des cases du morpion
    cpt = 0                                                                                                                                       # Compteur du nombre de cases jouées 

    # Vérifier si le texte de tous les boutons est vide
    for button in game_buttons:
        if button.cget("text") != "":
            cpt += 1 # Incrémente le nombre de cases jouées
    
    # Si c'est le premier tour de l'IA
    if cpt == 1:
        # Si le centre n'est pas joué, l'IA joue au centre (coup le plus pertinent)
        if game_button5.cget("text") == "":
            game_button5.configure(text = token_AI)
        # Sinon, l'IA joue une case aléatoire
        else: 
            # Toutes les cases sauf celle du milieu
            available_buttons = [button for button in game_buttons if button != game_button5]

            # Choisir au hasard un bouton parmi ceux disponibles
            random_button = random.choice(available_buttons)
            random_button.configure(text = token_AI)
    # Sinon si c'est en cours de partien, on calcule le meilleur coup à jouer pour l'IA
    elif cpt > 1 and cpt <= 9:
        # Meilleur case à jouer
        result = bestMove()

        # Case jouée par l'IA en fonction du résultat de bestMove
        bouton = globals()["game_button{}".format(result)]
        bouton.configure(text=token_AI)

        # Recherche de victoire pour l'IA
        result_AI = checkWin(token_AI)

        # Si l'IA a gagné, affichage d'un message et fin de partie
        if result_AI:
            game_history[1] = game_history[1] + 1
            win2_label.configure(text="Win AI : " + str(game_history[1]))
            messagebox.showinfo(title=None, message="Defeat !!!")
            reset()

            # Changement de joueur qui commence
            switchPlayer()
        # Sinon, si ce n'est pas gagné, mais que toutes les cases sont jouées, égalité
        elif all(button.cget("text") != "" for button in game_buttons):
            game_history[2] = game_history[2] + 1
            equality_label.configure(text="Equality : " + str(game_history[2]))
            messagebox.showinfo(title=None, message="Equality !!!")
            reset()

            # Changement de joueur qui commence
            switchPlayer()

def tic_tac_toe(elt):
    """! Jeu du morpion

    Fonction pour jouer au morpion depuis l'interface.

    @param elt: Case à jouer
    @type elt: Number

    """

    global first_player

    # Utilisation de globals() pour accéder aux variables globales par leur nom
    bouton = globals()["game_button{}".format(elt)]

    # Si la case n'a pas été jouée, elle est jouée
    if bouton.cget("text") == "":
        # Positionnement du pion du joueur
        bouton.configure(text=token_player)

        # Recherche de victoire du joueur et de l'IA
        result_player = checkWin(token_player)
        result_AI = checkWin(token_AI)

        # Si le joueur a gagné, affichage d'un message et fin de partie
        if result_player:
            game_history[0] = game_history[0] + 1
            win1_label.configure(text="Win player : " + str(game_history[0]))
            messagebox.showinfo(title=None, message="Victory !!!")        
            reset()

            # Changement de joueur qui commence
            switchPlayer()
        # Sinon, si l'IA a gagné, affichage d'un message et fin de partie
        elif result_AI:
            game_history[1] = game_history[1] + 1
            win2_label.configure(text="Win AI : " + str(game_history[1]))
            messagebox.showinfo(title=None, message="Defeat !!!")
            reset()

            # Changement de joueur qui commence
            switchPlayer()
        # Sinon, au tour de l'IA de jouer
        else:
            # Initialisation de variables
            game_buttons = [game_button1, game_button2, game_button3, game_button4, game_button5, game_button6, game_button7, game_button8, game_button9] # Liste des cases du morpion

            # Si toutes les cases sont jouées, égalité
            if all(button.cget("text") != "" for button in game_buttons):
                game_history[2] = game_history[2] + 1
                equality_label.configure(text="Equality : " + str(game_history[2]))
                messagebox.showinfo(title=None, message="Equality !!!")
                reset()

                # Changement de joueur qui commence
                switchPlayer()
            # Sinon, l'IA joue
            else:
                AI_play()
            
def start():
    """! Lancement d'une partie

    Fonction pour lancer une partie de morpion en initialisant tous les paramètres.

    """

    # Application de styles
    button_reset.configure(cursor="hand2", state="normal")
    button_start.configure(cursor="arrow", state="disabled")
    combobox1.configure(cursor="arrow", state="disabled")
    combobox2.configure(cursor="arrow", state="disabled")
    game_button1.configure(cursor="hand2", state="normal")
    game_button2.configure(cursor="hand2", state="normal")
    game_button3.configure(cursor="hand2", state="normal")
    game_button4.configure(cursor="hand2", state="normal")
    game_button5.configure(cursor="hand2", state="normal")
    game_button6.configure(cursor="hand2", state="normal")
    game_button7.configure(cursor="hand2", state="normal")
    game_button8.configure(cursor="hand2", state="normal")
    game_button9.configure(cursor="hand2", state="normal")

    # Si c'est à l'IA de jouer en première, elle joue
    if first_player == "AI":
        # Initialisation de variables
        game_buttons = [game_button1, game_button2, game_button3, game_button4, game_button5, game_button6, game_button7, game_button8, game_button9] # Liste des cases du morpion

        # Choisir au hasard un bouton parmi ceux disponibles
        random_button = random.choice(game_buttons)
        random_button.configure(text = token_AI)

def reset():
    """! Réinitialisation de la partie en cours

    Fonction pour réinitialiser la partie de morpion en cours et réinitialisant les paramètres.

    """

    # Application de styles
    button_reset.configure(cursor="arrow", state="disabled")
    button_start.configure(cursor="hand2", state="normal")
    combobox1.configure(cursor="hand2", state="normal")
    combobox2.configure(cursor="hand2", state="normal")
    game_button1.configure(cursor="arrow", state="disabled", text="")
    game_button2.configure(cursor="arrow", state="disabled", text="")
    game_button3.configure(cursor="arrow", state="disabled", text="")
    game_button4.configure(cursor="arrow", state="disabled", text="")
    game_button5.configure(cursor="arrow", state="disabled", text="")
    game_button6.configure(cursor="arrow", state="disabled", text="")
    game_button7.configure(cursor="arrow", state="disabled", text="")
    game_button8.configure(cursor="arrow", state="disabled", text="")
    game_button9.configure(cursor="arrow", state="disabled", text="")

# Création de la fenêtre principale
root = tk.Tk()
root.title("TIC-TAC-TOE game")

# Définition de la largeur et de la hauteur de la fenêtre
width = 1000
height = 500

# Styles de l'interface
background_color = "lightgrey"      # Couleur du fond de l'interface
border_color = "black"              # Couleur de la bordure entre la partie des paramètres/filtres et de la partie de jeu de l'interface
title_color = "black"               # Couleur du titre de la partie des paramètres/filtres
buttonActivated_color = "grey"      # Couleur du bouton actif
button_color = "lightgrey"          # Couleur des boutons des paramètres/filtres de l'interface
tictactoeBorder_color = "black"     # Couleur de la grille du morpion
tictactoeButton_color = "lightgrey" # Couleur des boutons de la partie de jeu de l'interface 
startButton_color = "lightgrey"     # Couleur du bouton Start

# Variables de jeu
token_player = "X"        # Pion du joueur
token_AI = "0"            # Pion de l'IA
game_history = [0,0,0,0]  # Tableau d'historique des parties (Victoires du joueur, Victoires de l'IA, égalité et nombre de parties)
first_player = "player"   # Joueur qui commence (player ou AI)
difficulty = "easy"       # Difficulté de l'IA (facile ou difficile)

# Récupérer les dimensions de l'écran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcul des coordonnées pour centrer la fenêtre
x = (screen_width - width) // 2
y = (screen_height - height) // 2

# Définir la position et les dimensions de la fenêtre
root.geometry(f"{width}x{height}+{x}+{y}")

# Création des trois frames
leftCol = tk.Frame(root, width=width*1 / 4, height=height)
rightCol = tk.Frame(root, width=width*3 / 4, height=height)

# Placement des cadres dans la fenêtre
leftCol.grid(row=0, column=0, rowspan=2, sticky="nsew")
rightCol.grid(row=0, column=2, rowspan=2, sticky="nsew")

# Sous-frame dans la partie gauche de l'interface
leftCol_content = tk.Frame(leftCol, padx=20, pady=20)
leftCol_content.place(relwidth=1, relheight=1)

leftCol_border = tk.Frame(leftCol_content, padx=2, pady=2)
leftCol_border.place(relwidth=1, relheight=1)
leftCol_border.configure(bg=border_color)

# Contenu de la partie gauche de l'interface
leftCol_subcontent = tk.Frame(leftCol_border)
leftCol_subcontent.place(relwidth=1, relheight=1)

# Style à appliquer sur des titres
subtitle = font.Font(family="Helvetica", size=14, weight="bold")

# Sous-titre de la partie gauche de l'interface
filter_label = tk.Label(leftCol_subcontent, text="Filters", padx=5, pady=5, font=subtitle)
filter_label.pack(side="top", anchor="n", pady=(10,10))

# Frame de boutons de la partie gauche de l'interface
filter_frame = tk.Frame(leftCol_subcontent)
filter_frame.pack(side="top", fill="both", expand=True)

# Variables pour les styles des boutons de filtre
filter_buttonHeight = 2
filter_buttonWidth = 8
filter_buttonMargin = 5

# Boutons pour les filtres
filter_button1 = tk.Button(filter_frame, text="Basic", width=filter_buttonWidth, height=filter_buttonHeight, cursor="hand2")
filter_button2 = tk.Button(filter_frame, text="Original", width=filter_buttonWidth, height=filter_buttonHeight, cursor="hand2")
filter_button3 = tk.Button(filter_frame, text="Light", width=filter_buttonWidth, height=filter_buttonHeight, cursor="hand2")
filter_button4 = tk.Button(filter_frame, text="Dark", width=filter_buttonWidth, height=filter_buttonHeight, cursor="hand2")
filter_button1.grid(row=0, column=0, padx=filter_buttonMargin, pady=filter_buttonMargin)
filter_button2.grid(row=0, column=1, padx=filter_buttonMargin, pady=filter_buttonMargin)
filter_button3.grid(row=1, column=0, padx=filter_buttonMargin, pady=filter_buttonMargin)
filter_button4.grid(row=1, column=1, padx=filter_buttonMargin, pady=filter_buttonMargin)
filter_button1.config(state="disabled", cursor="arrow")
filter_button1.configure(command=lambda: on_change_filter("Basic"), bg=buttonActivated_color)
filter_button2.configure(command=lambda: on_change_filter("Original"),bg=button_color)
filter_button3.configure(command=lambda: on_change_filter("Light"), bg=button_color)
filter_button4.configure(command=lambda: on_change_filter("Dark"), bg=button_color)

# Conteneur des listes déroulantes pour le choix du pion des joueurs
container = tk.Frame(leftCol_subcontent)
container.pack(anchor="w")

subcontainer1 = tk.Frame(container)
subcontainer1.pack(anchor="w")

# Label du choix des pions
label1 = tk.Label(subcontainer1, text=f"Token :", padx=5, pady=5)
label1.pack(side="left")

# Liste déroulante du choix du pion
combobox1 = ttk.Combobox(subcontainer1, values=["X", "0"])
combobox1.pack(side="left", padx=10)
combobox1.bind("<<ComboboxSelected>>", on_select_token)
combobox1.set("X")

subcontainer2 = tk.Frame(container)
subcontainer2.pack(anchor="w")

# Label du choix de la difficulté
label2 = tk.Label(subcontainer2, text=f"Difficulty :", padx=5, pady=5)
label2.pack(side="left")

# Liste déroulante du choix de la difficulté
combobox2 = ttk.Combobox(subcontainer2, values=["Easy", "Hard"])
combobox2.pack(side="left", padx=10)
combobox2.bind("<<ComboboxSelected>>", on_select_difficulty)
combobox2.set("Easy")

# Barre horizontale pour séparer les filtres de l'historique
separator = ttk.Separator(leftCol_subcontent, orient="horizontal")
separator.pack(fill="x", padx=20, pady=(10, 0))

# Sous-titre de la partie gauche de l'interface
game_history_label = tk.Label(leftCol_subcontent, text="History", padx=5, pady=5, font=subtitle, foreground=title_color)
game_history_label.pack(anchor="n", pady=(10,10))

# Historique des précédentes parties
win1_label = tk.Label(leftCol_subcontent, text="Win player : " + str(game_history[0]), padx=5, pady=5)
win1_label.pack(anchor="w")
win2_label = tk.Label(leftCol_subcontent, text="Win AI : " + str(game_history[1]), padx=5, pady=5)
win2_label.pack(anchor="w")
equality_label = tk.Label(leftCol_subcontent, text="Equality : " + str(game_history[2]), padx=5, pady=5)
equality_label.pack(anchor="w", pady=(0,10))

# Sous-frame dans la partie droite de l'interface
rightCol_content = tk.Frame(rightCol, padx=20, pady=20)
rightCol_content.place(relwidth=1, relheight=1)

# Frame pour simuler le plateau de jeu. Plateau de jeu composé de boutons
game_frame = tk.Frame(rightCol_content)
game_frame.pack(side="top", fill="both", expand=True)
game_frame.place(relx=0.5, rely=0.45, anchor="center")
game_frame.configure(bg=border_color)

# Variables pour les styles des boutons de jeu
game_buttonHeight = 4
game_buttonWidth = 8
game_buttonMargin = 3

# Boutons pour jouer
game_button1 = tk.Button(game_frame, width=game_buttonWidth, height=game_buttonHeight, state="disabled")
game_button2 = tk.Button(game_frame, width=game_buttonWidth, height=game_buttonHeight, state="disabled")
game_button3 = tk.Button(game_frame, width=game_buttonWidth, height=game_buttonHeight, state="disabled")
game_button4 = tk.Button(game_frame, width=game_buttonWidth, height=game_buttonHeight, state="disabled")
game_button5 = tk.Button(game_frame, width=game_buttonWidth, height=game_buttonHeight, state="disabled")
game_button6 = tk.Button(game_frame, width=game_buttonWidth, height=game_buttonHeight, state="disabled")
game_button7 = tk.Button(game_frame, width=game_buttonWidth, height=game_buttonHeight, state="disabled")
game_button8 = tk.Button(game_frame, width=game_buttonWidth, height=game_buttonHeight, state="disabled")
game_button9 = tk.Button(game_frame, width=game_buttonWidth, height=game_buttonHeight, state="disabled")
game_button1.grid(row=0, column=0, padx=(0,game_buttonMargin), pady=(0,game_buttonMargin))
game_button2.grid(row=0, column=1, padx=game_buttonMargin, pady=(0,game_buttonMargin))
game_button3.grid(row=0, column=2, padx=(game_buttonMargin,0), pady=(0,game_buttonMargin))
game_button4.grid(row=1, column=0, padx=(0,game_buttonMargin), pady=game_buttonMargin)
game_button5.grid(row=1, column=1, padx=game_buttonMargin, pady=game_buttonMargin)
game_button6.grid(row=1, column=2, padx=(game_buttonMargin,0), pady=game_buttonMargin)
game_button7.grid(row=2, column=0, padx=(0,game_buttonMargin), pady=(game_buttonMargin,0))
game_button8.grid(row=2, column=1, padx=game_buttonMargin, pady=(game_buttonMargin,0))
game_button9.grid(row=2, column=2, padx=(game_buttonMargin,0), pady=(game_buttonMargin,0))
game_button1.configure(command=lambda: tic_tac_toe("1"))
game_button2.configure(command=lambda: tic_tac_toe("2"))
game_button3.configure(command=lambda: tic_tac_toe("3"))
game_button4.configure(command=lambda: tic_tac_toe("4"))
game_button5.configure(command=lambda: tic_tac_toe("5"))
game_button6.configure(command=lambda: tic_tac_toe("6"))
game_button7.configure(command=lambda: tic_tac_toe("7"))
game_button8.configure(command=lambda: tic_tac_toe("8"))
game_button9.configure(command=lambda: tic_tac_toe("9"))

# Frame pour simuler le plateau de jeu. Plateau de jeu composé de boutons
manageGame_frame = tk.Frame(rightCol_content)
manageGame_frame.pack(side="top", fill="both", expand=True)
manageGame_frame.place(relx=0.5, rely=0.9, anchor="center")

# Boutons pour lancer et réinitialiser une partie
button_reset = tk.Button(manageGame_frame, text="Reset", width=10, height=2, cursor="hand2", state="disabled")
button_start = tk.Button(manageGame_frame, text="Start", width=10, height=2, cursor="hand2", state="normal")
button_reset.grid(row=0, column=0, padx=(0,20), pady=(0,0))
button_start.grid(row=0, column=1, padx=(20,0), pady=(0,0))
button_reset.configure(command=lambda: reset())
button_start.configure(command=lambda: start())

# Bloquer le redimensionnement de la fenêtre
root.resizable(0, 0)

# Lancer la boucle principale
root.mainloop()