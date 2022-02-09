import React from "react";
import {Link} from "react-router-dom";

export default function Header(){

    const dropdownbutton = (
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
        </button>
    )

    const searchform = (
        <form method="get" className="form-inline my-2 my-lg-0" action="/search/">
            <input class="form-control mr-sm-2" type="search" placeholder="Search" name="q" aria-label="Search"/>
            <button className="btn btn-outline-secondary my-2 my-sm-0" type="submit">Search</button>
        </form>
    )


    return(
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <a className="navbar-brand" href="">ShoppingWebsite</a>
            {dropdownbutton}
            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="navbar-nav mr-auto">
                    
                    <Navbaritem name="Home" href="/"/>

                    <Navbaritem name="Cart" href=""/>
                
                    <li className="nav-item dropdown">
                    <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Settings
                    </a>
                        <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                            <Dropdownarea href="" name="Profile"/>
                            <Dropdownarea href="" name="Edit profile"/>
                            <Dropdownarea href="" name="Change password"/>
                            <div className="dropdown-divider"></div>
                            <Dropdownarea href="" name="Orders"/>
                            <Dropdownarea href="" name="Add Product"/>
                            <Dropdownarea href="" name="Add Category"/>
                            <div className="dropdown-divider"></div>
                            <Dropdownarea href="" name="Logout"/>
                            <Dropdownarea href="" name="Login"/>
                            <Dropdownarea href="" name="Signup"/>
                        </div>
                    </li>
                </ul>
                {searchform}
            </div>
        </nav>
    );
}


function Navbaritem(props){
    return(
        <li className="nav-item">
          <Link className="nav-link" to={props.href}>{props.name}</Link>
        </li>

    );
}

function Dropdownarea(props){
    return(
        <Link className="dropdown-item" to={props.href}>{props.name}</Link>
    )

}
