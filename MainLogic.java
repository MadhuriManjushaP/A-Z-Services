package naveen;
import java.util.Scanner;

public class MainLogic {
	
//execution starts from here
		public static void main(String[] args) {
//string array			
	String names[]={"hoarseness","swelling",
	"heavybreathing",
	"dizziness","neckvein"};
//	advanced for loop for iterating elements in array
	for(String name : names) 
	{
//if condition satisfies then only enters into loop
	if(name.equals("Hoarseness") || name.equals("hoarseness"))
	{
	System.out.println("when do you feel Hoarseness?");
//	taking input from the user
	Scanner sc = new Scanner(System.in);
	String a = sc.nextLine();
	System.out.println("Okay,Do you have any swelling over neck?");
//	logic written inside do while loop if user did not enter the specified things in the below if condition then it will show error message ,as it mentioned in the below print statement 
//and asks user to re-enter the input again	
int count=0;
//in do while first enters into loop after that checks for while condition ,if it satisfies then renters 
//	into the loop ,otherwise exists from the loop
do
	{

	Scanner b = new Scanner(System.in);
	String c=b.nextLine();

	if(c.equals("yes") || c.equals("no") || c.equals("nope"))
	{
	System.out.println("Are you suffering from cough");
	count++;
	}
	else{
	System.out.println("i don't understand plz enter again / do you have any swelling over neck");
	}
	}while(count==0); 
//if condition was satisfied then counter will increase and exists from the while loop ..otherwise ask the user to re enter the input again in yes/no format
	int count0=0;
//	this flow will continue to the all the sympotms mentioned below
	do
	{

	Scanner d = new Scanner(System.in);
	String e=sc.nextLine();

	if(e.equals("yes") || e.equals("no") || e.equals("nope"))
	{
	System.out.println("is there any dizziness when you raised your arms");
	count0++;
	}
	else{
	System.out.println("i don't understand plz enter again / are you suffering from cough");
	}
	}while(count0==0);
	int count1=0;
	do
	{

	Scanner f = new Scanner(System.in);
	String g=f.nextLine();

	if(g.equals("yes") || g.equals("no") || g.equals("nope"))
	{
	System.out.println("did you feel any neck vein");
	count1++;
	}
	else{
	System.out.println("i don't understand plz enter again / is there any dizziness when you raised your arms");
	}
	}while(count1==0);
	int count2=0;
	do
	{

	Scanner h = new Scanner(System.in);
	String i=h.nextLine();

	if(i.equals("yes") || i.equals("no") || i.equals("nope"))
	{
	System.out.println("it seems you have goiter ,please consult doctor as soon as possible");
	count2++;
	}
	else{
	System.out.println("i don't understand plz enter again / did you feel neck vein");
	}
	}while(count2==0);
	break;
//the program will terminate here ,based on keyword matches from the string array ,those set of conversations will raises and terminates by using break statement at the end of conversations
	}

	if(name.equals("Swelling") || name.equals("swelling"))
	{
	System.out.println("when did you start obseving the change?");
	Scanner sc = new Scanner(System.in);
	String a = sc.nextLine();
	System.out.println("Okay,is there any dizziness when you raise your hand above the head?");
	int count=0;
	do
	{

	Scanner b = new Scanner(System.in);
	String c=b.nextLine();

	if(c.equals("yes") || c.equals("no") || c.equals("nope"))
	{
	System.out.println("Did you observe any weight loss?");
	count++;
	}
	else{
	System.out.println("i don't understand plz enter again / is there any dizziness when you raise your hand above the head");
	}
	}while(count==0);
	int count0=0;
	do
	{

	Scanner d = new Scanner(System.in);
	String e=sc.nextLine();

	if(e.equals("yes") || e.equals("no") || e.equals("nope"))
	{
	System.out.println("is there heavy sweting?");
	count0++;
	}
	else{
	System.out.println("i don't understand plz enter again / did you observe any weight loss");
	}
	}while(count0==0);
	int count1=0;
	do
	{

	Scanner f = new Scanner(System.in);
	String g=f.nextLine();

	if(g.equals("yes") || g.equals("no") || g.equals("nope"))
	{
	System.out.println("did you feel any neck vein");
	count1++;
	}
	else{
	System.out.println("i don't understand plz enter again / is there heavy sweting");
	}
	}while(count1==0);
	int count2=0;
	do
	{

	Scanner h = new Scanner(System.in);
	String i=h.nextLine();

	if(i.equals("yes") || i.equals("no") || i.equals("nope"))
	{
	System.out.println("it seems you have goiter ,please consult doctor as soon as possible");
	count2++;
	}
	else{
	System.out.println("i don't understand plz enter again / did you feel neck vein");
	}
	}while(count2==0);
	break;

	}

	if(name.equals("heavybreathing") || name.equals("heavy breathing"))
	{
	System.out.println("Do you face difficulty in breathing only when running, walking or all the time??");
	Scanner sc = new Scanner(System.in);
	String a = sc.nextLine();
	System.out.println("Okay,Do you have any swelling over neck?");
	int count=0;
	do
	{

	Scanner b = new Scanner(System.in);
	String c=b.nextLine();

	if(c.equals("yes") || c.equals("no") || c.equals("nope"))
	{
	System.out.println("is there any dizziness when you raised your arms above the head?");
	count++;
	}
	else{
	System.out.println("i don't understand plz enter again / do you have any swelling over neck");
	}
	}while(count==0);
	int count0=0;
	do
	{

	Scanner d = new Scanner(System.in);
	String e=sc.nextLine();

	if(e.equals("yes") || e.equals("no") || e.equals("nope"))
	{
	System.out.println("Did you obseved any weight loss?");
	count0++;
	}
	else{
	System.out.println("i don't understand plz enter again / is there any dizziness when you raised your arms above the head");
	}
	}while(count0==0);
	int count1=0;
	do
	{

	Scanner f = new Scanner(System.in);
	String g=f.nextLine();

	if(g.equals("yes") || g.equals("no") || g.equals("nope"))
	{
	System.out.println("did sweating is heavy?");
	count1++;
	}
	else{
	System.out.println("i don't understand plz enter again / Did you obseved any weight loss");
	}
	}while(count1==0);
	int count2=0;
	do
	{

	Scanner h = new Scanner(System.in);
	String i=h.nextLine();

	if(i.equals("yes") || i.equals("no") || i.equals("nope"))
	{
	System.out.println("it seems you have goiter ,please consult doctor as soon as possible");
	count2++;
	}
	else{
	System.out.println("i don't understand plz enter again / did sweating is heaavy");
	}
	}while(count2==0);
	break;

	}

	if(name.equals("dizziness") || name.equals("Dizzinness"))
	{
	System.out.println(".When do you feel dizzy?Only when you raise your arms or all the time?");
	Scanner sc = new Scanner(System.in);
	String a = sc.nextLine();
	System.out.println("Okay,Do you have any swelling over neck?");
	int count=0;
	do
	{

	Scanner b = new Scanner(System.in);
	String c=b.nextLine();

	if(c.equals("yes") || c.equals("no") || c.equals("nope"))
	{
	System.out.println("Are you suffering from cough");
	count++;
	}
	else{
	System.out.println("i don't understand plz enter again / Do you have any swelling over neck");
	}
	}while(count==0);
	int count0=0;
	do
	{

	Scanner d = new Scanner(System.in);
	String e=sc.nextLine();

	if(e.equals("yes") || e.equals("no") || e.equals("nope"))
	{
	System.out.println("Did you observe any weight loss?");
	count0++;
	}
	else{
	System.out.println("i don't understand plz enter again / Are you suffering from cough ");
	}
	}while(count0==0);
	int count1=0;
	do
	{

	Scanner f = new Scanner(System.in);
	String g=f.nextLine();

	if(g.equals("yes") || g.equals("no") || g.equals("nope"))
	{
	System.out.println("did you feel any neck vein");
	count1++;
	}
	else{
	System.out.println("i don't understand plz enter again / Did you observe any weight loss");
	}
	}while(count1==0);
	int count2=0;
	do
	{

	Scanner h = new Scanner(System.in);
	String i=h.nextLine();

	if(i.equals("yes") || i.equals("no") || i.equals("nope"))
	{
	System.out.println("it seems you have goiter ,please consult doctor as soon as possible");
	count2++;
	}
	else{
	System.out.println("i don't understand plz enter again / did you feel any neck vein");
	}
	}while(count2==0);
	break;

	}

	if(name.equals("neckvein") || name.equals("neck vein"))
	{
	System.out.println("From how many days you are suffering from that?");
	Scanner sc = new Scanner(System.in);
	String a = sc.nextLine();
	System.out.println("Okay,Do you have any swelling over neck?");
	int count=0;
	do
	{

	Scanner b = new Scanner(System.in);
	String c=b.nextLine();

	if(c.equals("yes") || c.equals("no") || c.equals("nope"))
	{
	System.out.println("did sweting is heavy?");
	count++;
	}
	else{
	System.out.println("i don't understand plz enter again / Do you have any swelling over neck");
	}
	}while(count==0);
	int count0=0;
	do
	{

	Scanner d = new Scanner(System.in);
	String e=sc.nextLine();

	if(e.equals("yes") || e.equals("no") || e.equals("nope"))
	{
	System.out.println("is there any dizziness when you raised your arms");
	count0++;
	}
	else{
	System.out.println("i don't understand plz enter again / did sweting is heavy");
	}
	}while(count0==0);
	int count1=0;
	do
	{

	Scanner f = new Scanner(System.in);
	String g=f.nextLine();

	if(g.equals("yes") || g.equals("no") || g.equals("nope"))
	{
	System.out.println("did u have hoarsenss(husky/rough throat)");
	count1++;
	}
	else{
	System.out.println("i don't understand plz enter again / is there any dizziness when you raised your arms");
	}
	}while(count1==0);
	int count2=0;
	do
	{

	Scanner h = new Scanner(System.in);
	String i=h.nextLine();

	if(i.equals("yes") || i.equals("no") || i.equals("nope"))
	{
	System.out.println("it seems you have goiter ,please consult doctor as soon as possible");
	count2++;
	}
	else{
	System.out.println("i don't understand plz enter again / did u have hoarsenss(husky/rough throat)");
	}
	}while(count2==0);
	break;

	}}}}



