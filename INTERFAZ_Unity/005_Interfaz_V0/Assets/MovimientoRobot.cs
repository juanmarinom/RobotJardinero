using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovimientoRobot: MonoBehaviour
{
    Vector3 targetpos;
    Vector3 currentPos;
    // Start is called before the first frame update
    void Start()
    {
        targetpos.x = 100;
        targetpos.y = 100;
        targetpos.z = 0;
        // transform.position = targetpos;
        currentPos = targetpos;

    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.A))
        {
            currentPos.x = currentPos.x - 20;
            transform.position = currentPos;
        }
        if (Input.GetKeyDown(KeyCode.D))
        {
            currentPos.x = currentPos.x + 20;
            transform.position = currentPos;
        }
        if (Input.GetKeyDown(KeyCode.W))
        {
            currentPos.y = currentPos.y + 20;
            transform.position = currentPos;
        }
        if (Input.GetKeyDown(KeyCode.S))
        {
            currentPos.y = currentPos.y - 20;
            transform.position = currentPos;
        }
    }
}

