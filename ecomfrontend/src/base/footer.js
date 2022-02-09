import React from "react";

export default function Footer(){
    const footerstyle ={
        "background-color":"#f8f9fa",
        clear: "both",
        position: "relative",
        height: "100px",
    }
    return(
        <div className="container">
            <footer style={footerstyle} className="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
                <p className="col-md-4 mb-0 text-muted">2022 Company, Inc</p>
                <ul className="nav col-md-4 justify-content-end">
                    <Footeritem href="" name="Home"/>
                    <Footeritem href="" name="Cart"/>
                    <Footeritem href="" name="Profile"/>
                    <Footeritem href="" name="Orders"/>
                </ul>
            </footer>
        </div>

    );
}

function Footeritem(props){
    return(
      <li className="nav-item"><a href={props.href} className="nav-link px-2 text-muted">{props.name}</a></li>
    )
}