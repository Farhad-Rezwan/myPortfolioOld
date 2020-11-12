import React from "react"
import { FaCode, FaAppStoreIos, FaAndroid } from "react-icons/fa"
export default [
  {
    id: 1,
    icon: <FaCode className="service-icon" />,
    title: "web development",
    text: `REACT, NodeJS, Strapi, Gatsby, AWS and others`,
  },
  {
    id: 2,
    icon: <FaAppStoreIos className="service-icon" />,
    title: "iOS Development",
    text: `SWIFT, refer to iOS projects in Projects section`,
  },
  {
    id: 3,
    icon: <FaAndroid className="service-icon" />,
    title: "Android Development",
    text: `Android, refer to android sample projects in Projects section`,
  }
]
