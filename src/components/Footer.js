import React from "react"
import SocialLinks from "../constants/socialLinks"
const Footer = () => {
  return <footer className="footer">
    <div>
      <SocialLinks className="footer-links"/>
      <h4>copyright&copy;{new Date().getFullYear()}
        <span>WebDev</span>
      </h4>
    </div>
  </footer>
}

export default Footer
