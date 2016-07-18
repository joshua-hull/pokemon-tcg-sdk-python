# Pokemon TCG SDK

This is a Python implementation of an SDK for the Pokemon TCG. It is a wrapper around the Pokemon TCG API of [pokemontcg.io](http://pokemontcg.io/). It is based heavily off the [Magic: The Gathering SDK](http://github.com/MagicTheGathering/mtg-sdk-python).

## Usage

Import (Card and Set are probably what you'll want most)

```python
from pokemonsdk import Card
from pokemonsdk import Set
from pokemonsdk import Type
from pokemonsdk import Supertype
from pokemonsdk import Subtype
```

### Properties Per Class
#### Card
```python
id
name
image_url
subtype
supertype
ability
hp
retreat_cost
number
artist
rarity
series
set
set_code
types
attacks
weaknesses
resistances
```

#### Set
```python
code
name
series
total_cards
standard_legal
release_date
```

### Find Card by Id

    card = Card.find(xy7-54)

### Filter Cards via Query Parameters

    cards = Card.where(types='metal,psychic').all()

### Get all cards (will page through all the data - could take awhile)

    cards = Card.all()

### Get all cards, but only a specific page of data

    cards = Card.where(page=5).where(pageSize=1000).all()

### Find a Set by code

    set = Set.find('xy1')

### Get all sets

    sets = Set.all()

### Filter sets via query parameters

    sets = Set.where(name='jungle').all()

### Get all types

    types = Type.all()

### Get all subtypes

    subtypes = Subtype.all()

### Get all supertypes

    supertypes = Supertype.all()
