""" datos importantes de cada receta/comida:
# - name (nombre de la receta)
# - id
# - description (breve descripción de la receta)
# - thumbnail_url (foto de la receta)
# - prep_time_minutes
# - cook_time_minutes
# - num_servings
# - instructions
# - sections
# - user_ratings
# - total_ratings
# - video_url (video de la food)
# - price (precios en una structura de datos)
# - ingredients
# - nutrition
"""
class Food:
    def __init__(self, name, id, description, thumbnail_url, prep_time_minutes, cook_time_minutes, num_servings, instructions, sections, user_ratings, video_url, price, ingredients, nutrition):
        self.name = name
        self.id = id
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.prep_time_minutes = prep_time_minutes
        self.cook_time_minutes = cook_time_minutes
        self.num_servings = num_servings
        self.instructions = instructions
        self.sections = sections
        self.user_ratings = user_ratings
        self.video_url = video_url
        self.price = price
        self.ingredients = ingredients
        self.nutrition = nutrition
    
    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_description(self):
        return self.description

    def get_thumbnail_url(self):
        return self.thumbnail_url

    def get_prep_time_minutes(self):
        return self.prep_time_minutes

    def get_cook_time_minutes(self):
        return self.cook_time_minutes

    def get_num_servings(self):
        return self.num_servings

    def get_instructions(self):
        return self.instructions

    def get_sections(self):
        return self.sections

    def get_user_ratings(self):
        return self.user_ratings

    def get_video_url(self):
        return self.video_url

    def get_price(self):
        return self.price

    def get_ingredients(self):
        return self.ingredients

    def get_nutrition(self):
        return self.nutrition
    def __str__(self):
        return f"Food(name={self.name}, id={self.id}, description={self.description}, thumbnail_url={self.thumbnail_url}, prep_time_minutes={self.prep_time_minutes}, cook_time_minutes={self.cook_time_minutes}, num_servings={self.num_servings}, instructions={self.instructions}, sections={self.sections}, user_ratings={self.user_ratings}, video_url={self.video_url}, price={self.price}, ingredients={self.ingredients}, nutrition={self.nutrition})"
