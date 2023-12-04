import React, { useState} from "react";
//import { hero } from "/src/data";
import { Card } from "/src/components/hero/card";
import '/src/components/hero/hero.css';
import { useEffect } from "react";

export const Hero = () => {
    const [items, setItems] = useState([]);

    useEffect(() => {
        fetch("https://api.example.com/items")
          .then(res => res.json())
          .then(
            (result) => {
              setIsLoaded(true);
              setItems(result);
            }
          
          )
      }, [])
    return (
        <>
                <section className="hero">
                   
                    <div className="container">
                        {items.map((item) => {
                            return <Card key={item.id} items={item}></Card>
                         
                        })}
                    
                    </div>
                </section>
        </>
    )
}