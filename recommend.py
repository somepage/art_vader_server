import random
import json


def change_weights(label, like, prediction_rate = 0.05):
    with open('weights.json', 'r') as f:
        weights = json.load(f)
    if label not in weights.keys():
        return "Label is not defined"
    else:
        n = len(weights)
        if like:
            for value in weights.values():
                value += -prediction_rate / (n - 1)
            weights[label] += prediction_rate + prediction_rate / (n - 1)
        else:
            for value in weights.values():
                value += prediction_rate / (n - 1)
            weights[label] += -prediction_rate - prediction_rate / (n - 1)
        with open('weights.json', 'w', encoding='utf-8') as f:
            json.dump(weights, f, indent=4, ensure_ascii=False)

        return (random.choices(list(weights.keys()), weights=list(weights.values()))[0]).encode('utf-8')
