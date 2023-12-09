import React, { useState} from "react";
//import { popular } from "/src/data";
import { Newscard } from '/src/components/news/newscard';
import '/src/components/news/news.css';
import { useEffect } from "react";

export const News = () => {
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
                <section className="news">
                   
                    <div className="container">
                        {items.map((item) => {
                            return <Newscard key={item.id} items={item}></Newscard>
                         
                        })}
                    
                    </div>
                </section>
        </>
    )
}