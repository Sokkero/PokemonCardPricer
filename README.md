# Pokémon Card Pricer
This tool takes a card id (i.e. `dri081`) and a language key, which tells the program which language the card is in, and looks up the price of the given card in the given langauge using www.cardmarket.com. 

### Language keys:
| Key    | Language             |
|--------|----------------------|
| `en`   | English              |
| `fr`   | French               |
| `de`   | German               |
| `sp`   | Spanish              |
| `it`   | Italian              |
| `s-ch` | Mandarin             |
| `ja`   | Japanese             |
| `po`   | Polish               |
| `ko`   | Korean               |
| `t-ch` | Mandarin Traditional |

### About
The program uses a headless selenium browser that looks up the card prices for the provided card IDs in the given languages. 