public class Song {
    public static void main(String[] args) {
        fly_verse();
        System.out.println();
        spider_verse();
        System.out.println();
        bird_verse();
        System.out.println();
        cat_verse();
        System.out.println();
        dog_verse();
        System.out.println();
        fish_verse();
        System.out.println();
        horse_verse();
    }

    public static void last_lines() {
        System.out.println("I don't know why she swallowed that fly,");
        System.out.println("Perhaps she'll die.");
        }

    public static void spider_repeat() {
        System.out.println("She swallowed the spider to catch the fly,");
        }

    public static void bird_repeat() {
        System.out.println("She swallowed the bird to catch the spider,");
        }

    public static void cat_repeat() {
        System.out.println("She swallowed the cat to catch the bird,");
        }

    public static void dog_repeat() {
        System.out.println("She swallowed the dog to catch the cat,");
        }

    public static void fly_verse() {
        System.out.println("There was an old woman who swallowed a fly.");
        last_lines();
        }
    
    public static void spider_verse() {
        System.out.println("There was an old woman who swallowed a spider,");
        System.out.println("That wriggled and iggled and jiggled inside her.");
        spider_repeat();
        last_lines();
    }

    public static void bird_verse() {
        System.out.println("There was an old woman who swallowed a bird,");
        System.out.println("How absurd to swallow a bird.");
        bird_repeat();
        spider_repeat();
        last_lines();
    }

    public static void cat_verse() {
        System.out.println("There was an old woman who swallowed a cat,");
        System.out.println("Imagine that to swallow a cat.");
        cat_repeat();
        bird_repeat();
        spider_repeat();
        last_lines();
    }

    public static void dog_verse() {
        System.out.println("There was an old woman who swallowed a dog,");
        System.out.println("What a hog to swallow a dog.");
        dog_repeat();
        cat_repeat();
        bird_repeat();
        spider_repeat();
        last_lines();
    }

    public static void fish_verse() {
        System.out.println("There was an old woman who swallowed a fish,");
        System.out.println("What a dish to swallow a fish.");
        System.out.println("She swallowed the fish to catch the dog,");
        dog_repeat();
        cat_repeat();
        bird_repeat();
        spider_repeat();
        last_lines();
    }

    public static void horse_verse() {
        System.out.println("There was an old woman who swallowed a horse,");
        System.out.println("She died of course.");
    }
}
