class Bot:
    def get_decision(self, dealer_up_card, hand, dealer_prev_hand):
        sc = 0
        self.t = []
        for card in hand:
            if 2 <= card.rank and card.rank <= 9:
                sc += card.rank
            elif card.rank > 9:
                sc += 10
            elif card.rank == 1:
                sc += 11
            while sc > 21:
                sc -= 10
            for card in hand:
                self.t.append(card.rank)
            if len(self.t) == 2 and self.t[0] == 11:
                if self.t[1] == 9:
                    return "stand"
                elif self.t[1] == 8:
                    if dealer_up_card.rank == 6:
                        return "double down"
                elif self.t[1] == 7:
                    if 2 <= dealer_up_card.rank <= 6:
                        return "double down"
                    elif 9 <= dealer_up_card.rank <= 11:
                        return "hit"
                    else:
                        return "stand"
                elif self.t[1] == 6:
                    if 3 <= dealer_up_card.rank <= 6:
                        return "double down"
                    else:
                        return "hit"
                elif self.t[1] == 5 or self.t[1] == 4:
                    if 4 <= dealer_up_card.rank <= 6:
                        return "double down"
                    else:
                        return "hit"
                elif self.t[1] == 3 or self.t[1] == 2:
                    if 5 <= dealer_up_card.rank <= 6:
                        return "double down"
                    else:
                        return "hit"
        if sc >= 17:
            return "stand"
        elif 13 <= sc <= 16 and 2 <= dealer_up_card.rank <= 6:
            return "stand"
        elif sc == 12 and 4 <= dealer_up_card.rank <= 6:
            return "stand"
        elif sc == 11:
            return "double down"
        elif sc == 10 and 2 <= dealer_up_card.rank <= 9:
            return "double down"
        elif sc == 9 and 3 <= dealer_up_card.rank <= 6:
            return "double down"
        else:
            return "hit"
