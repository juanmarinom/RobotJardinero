using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class plant1_handler : MonoBehaviour
{
    public int maxHealth = 100;
    public int currentHealth;
    public HealthBar healthBar;
    
  
    void Start()
    {
        currentHealth = maxHealth;
        healthBar.SetMaxHealth(currentHealth);
    }

    // Update is called once per frame
    void Update()
    {
        if(Input.GetKeyDown(KeyCode.Space))
        {
            TakeDamage(20);
        }
        if (Input.GetKeyDown(KeyCode.A))
        {
            MoverSprite();
        }
    }
    void TakeDamage(int damage)
    {
        currentHealth -= damage;
        healthBar.SetHealth(currentHealth);
 
   }
    public void MoverSprite()
    {

        transform.Translate(Vector2.zero);
    }
}
