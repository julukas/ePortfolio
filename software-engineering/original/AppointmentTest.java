package contact;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Date;
public class AppointmentTest {
	@Test
	public void testAppointmentCreation() {
		Appointment appointment = new Appointment("1231231234",new Date(System.currentTimeMillis()+100000),"This is a sample task description");
		assertEquals("1231231234",appointment.getAppointmentID());
		assertNotNull(appointment.getAppointmentDate());
		assertEquals("This is a sample task description",appointment.getDescription());

	}
	@Test
	public void testInvalidContactCreation() {
		//test for null appt id
		assertThrows(IllegalArgumentException.class,()->{
			new Appointment(null,new Date(System.currentTimeMillis()+100000),"This is a sample task description");
		});
		//test for date in the past
		assertThrows(IllegalArgumentException.class,()->{
			new Appointment("1231231234",new Date(System.currentTimeMillis()-100000),"This is a sample task description");
		});
		//test for long id
		assertThrows(IllegalArgumentException.class,()->{
			new Appointment("12312312345555",new Date(System.currentTimeMillis()+100000),"This is a sample task description");
		});
		//test for null description
		assertThrows(IllegalArgumentException.class,()->{
			new Appointment("1231231234",new Date(System.currentTimeMillis()+100000),null);
		});
		//test for long description
		assertThrows(IllegalArgumentException.class,()->{
			new Appointment("1231231234",new Date(System.currentTimeMillis()+100000),"This is an ultra long description that will not fit within the character limit");
		});
		//test for null date
		assertThrows(IllegalArgumentException.class,()->{
			new Appointment("1231231234",null,"This is a sample task description");
		});
	}
}
