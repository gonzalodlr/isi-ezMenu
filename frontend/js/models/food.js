export class Food {
    constructor(food) {
        this.name = food.Name;
        this.id = food.ID;
        this.description = food.Description;
        this.thumbnailURL = food["Thumbnail_URL"];
        this.prepTimeMinutes = food["Prep Time Minutes"];
        this.cookTimeMinutes = food["Cook Time Minutes"];
        this.numServings = food["Num Servings"];
        this.instructions = food.Instructions;
        this.sections = food.Sections;
        this.userRatings = food["User Ratings"];
        this.videoURL = food["Video URL"];
        this.price = food.Price;
        this.ingredients = food.Ingredients;
        this.nutrition = food.Nutrition;
    }

    str() {
        return `Food: ${this.name}\nID: ${this.id}\nDescription: ${this.description}\nThumbnail URL: ${this.thumbnailURL}\nPrep Time (minutes): ${this.prepTimeMinutes}\nCook Time (minutes): ${this.cookTimeMinutes}\nNumber of Servings: ${this.numServings}\nInstructions: ${this.instructions}\nSections: ${this.sections}\nUser Ratings: ${this.userRatings}\nVideo URL: ${this.videoURL}\nPrice: ${this.price}\nIngredients: ${this.ingredients}\nNutrition: ${this.nutrition}`;
    }
}
