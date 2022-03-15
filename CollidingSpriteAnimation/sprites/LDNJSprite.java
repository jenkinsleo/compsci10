import java.awt.Image;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import java.lang.Math;


public class LDNJSprite implements DisplayableSprite, MovableSprite, CollidingSprite {

	Image image = null;
	private double centerX = 0;
	private double centerY = 0;
	private double width = 64;
	private double height = 64;
	
	private double velocityX = 0;
	private double velocityY = 0;
	
	private long score = 0;
	private static int SCORE_AMOUNT = 100;
	
	private boolean exitStatus = false;
	private String proximityMessage;
	
	public LDNJSprite(double x, double y) {
		super();

		if (image == null) {
			try {
				image = ImageIO.read(new File("res/ldnj/avatar.png"));
				
			}
			catch (IOException e) {
				System.out.println(e.toString());
			}
			
			
		}
		
		this.setCenterX(x);
		this.setCenterY(y);
		
	
	}
	
	public LDNJSprite() {
		this(0,0);
	}
	
	@Override
	public long getScore() {
		
		return this.score;
	}

	@Override
	public String getProximityMessage() {
		
		return this.proximityMessage;
	}

	@Override
	public boolean getIsAtExit() {
		
		return this.exitStatus;
	}

	@Override
	public void setCenterX(double centerX) {
		
		this.centerX = centerX;
	}

	@Override
	public void setCenterY(double centerY) {
		
		this.centerY = centerY;
	}

	@Override
	public void moveX(double pixelsPerSecond) {
		
		this.velocityX = pixelsPerSecond;
	}

	@Override
	public void moveY(double pixelsPerSecond) {
		this.velocityY = pixelsPerSecond;
	}

	@Override
	public void stop() {
		//not needed for this
		
	}

	@Override
	public Image getImage() {
		return this.image;
	}

	@Override
	public boolean getVisible() {
		return true;
	}

	@Override
	public double getMinX() {
		return this.centerX - (this.width / 2);
	}

	@Override
	public double getMaxX() {
		return this.centerX + (this.width / 2);
	}

	@Override
	public double getMinY() {
		return this.centerY - (this.height / 2);
	}

	@Override
	public double getMaxY() {
		return this.centerY + (this.height / 2);
	}

	@Override
	public double getHeight() {
		return this.height;
	}

	@Override
	public double getWidth() {
		return this.width;
	}

	@Override
	public double getCenterX() {
		return this.centerX;
	}

	@Override
	public double getCenterY() {
		return this.centerY;
	}

	@Override
	public boolean getDispose() {
		return false;
	}

	@Override
	public void update(Universe universe, KeyboardInput keyboard, long actual_delta_time) {
		
		double deltaX = actual_delta_time * 0.001 * velocityX;
		if (checkCollisionWithBarrier(universe, deltaX, 0) == false) {
			this.centerX += (this.velocityX * actual_delta_time) / 1000;
			}
		
		double deltaY = actual_delta_time * 0.001 * velocityY;
		if (checkCollisionWithBarrier(universe, 0, deltaY) == false) {
			this.centerY += (this.velocityY * actual_delta_time) / 1000;

		}
		
		coveringCoin(universe, deltaX, deltaY);
		insideExit(universe, deltaX,deltaY);
		makeMessage(universe, deltaX, deltaY);
		
	}

	private boolean checkCollisionWithBarrier(Universe sprites, double deltaX, double deltaY) {

		boolean colliding = false;

		for (DisplayableSprite sprite : sprites.getSprites()) {
			if (sprite instanceof BarrierSprite) {
				if (CollisionDetection.overlaps(this.getMinX() + deltaX, this.getMinY() + deltaY, 
						this.getMaxX()  + deltaX, this.getMaxY() + deltaY, 
						sprite.getMinX(),sprite.getMinY(), 
						sprite.getMaxX(), sprite.getMaxY())) {
					colliding = true;
					break;					
				}
			}
		}		
		return colliding;		
	}
	
	private void coveringCoin(Universe sprites, double deltaX, double deltaY) {

		for (DisplayableSprite sprite : sprites.getSprites()) {
			if (sprite instanceof CoinSprite) {
				if (CollisionDetection.covers(this.getMinX() + deltaX, this.getMinY() + deltaY, 
						this.getMaxX()  + deltaX, this.getMaxY() + deltaY, 
						sprite.getMinX(),sprite.getMinY(), 
						sprite.getMaxX(), sprite.getMaxY())) {
					//adds score and dispose coin
					this.score += SCORE_AMOUNT;
					((CoinSprite) sprite).setDispose(true);
					break;					
				}
			}
		}		
	}
	
	private void insideExit(Universe sprites, double deltaX, double deltaY) {
		for (DisplayableSprite sprite : sprites.getSprites()) {
			if (sprite instanceof ExitSprite) {
				if (CollisionDetection.inside(this.getMinX() + deltaX, this.getMinY() + deltaY, 
						this.getMaxX()  + deltaX, this.getMaxY() + deltaY, 
						sprite.getMinX(),sprite.getMinY(), 
						sprite.getMaxX(), sprite.getMaxY())) {
					this.exitStatus = true;
					
					break;					
				}
			}
		}
	}
	
	private void makeMessage(Universe sprites, double deltaX, double deltaY) {
		for (DisplayableSprite sprite: sprites.getSprites()) {
			if (sprite.getClass().toString().contains("CoinSprite") == false && sprite.getClass().toString().contains("BarrierSprite") == false && sprite.getClass().toString().contains("ExitSprite") == false) {
				if (sprite.getClass() != this.getClass()) {
					//check if within 100 pixels
					// formula is sqaure root of  y1-x1 squared + y2-x2 squared
					double x1 = this.centerX;
					double y1 = this.centerY;
					
					double x2 = sprite.getCenterX();
					double y2 = sprite.getCenterY();
					
					int distanceBetween = (int) Math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2- y1)));
					if (distanceBetween < 100) {
						this.proximityMessage = String.format("%s is close!", sprite.getClass().toString());
						this.proximityMessage = proximityMessage.substring(5, Math.min(proximityMessage.length(), 32));
					} else {
						this.proximityMessage = "";
					}
					
				}
			}
		}
	}






	
	
}
