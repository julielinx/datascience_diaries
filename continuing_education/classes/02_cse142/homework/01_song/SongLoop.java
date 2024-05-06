public class SongLoop{
    public static void main(String[] args) {
      forLoop();
    }
    
    public static void forLoop() {
      String[] animals = {"fly", "spider", "bird", "cat", "dog", "fish", "horse"};
      String[] animalSent = {"I don't know why she swallowed that fly,",
      "That wriggled and iggled and jiggled inside her.",
      "How absurd to swallow a bird.",
      "Imagine that to swallow a cat.",
      "What a hog to swallow a dog.",
      "What a dish to swallow a fish."
      };
      for (int i=0; i<6; i++) {
        System.out.println("There was an old woman who swallowed a " + animals[i] + ",");
        if (i>0) {
        System.out.println(animalSent[i]);};
        for (int j=i; j>0; j--) {
            System.out.println("She swallowed the " + animals[j] + " to catch the " + animals[j-1] + ",");
          };
        System.out.println("I don't know why she swallowed that fly,");
        System.out.println("Perhaps she'll die.");
        System.out.println();
        };
      System.out.println("There was an old woman who swallowed a " + animals[6] + ",");
      System.out.println("She died of course.");
    
      }
  }
  