import React from "react"
import { graphql } from "gatsby"
import Layout from "../components/Layout"
import Hero from "../components/Hero"
import Services from "../components/Services"
import Jobs from "../components/Jobs"
import Projects from "../components/Projects"
import Blogs from "../components/Blogs"

export default ({ data }) => {
    const {
        allStrapiProjects: { nodes: projects },
        allStrapiBlogs: { nodes: blogs },
    } = data

    return (
        <Layout>
            <Hero />
            <Services />
            <Jobs />
            <Projects projects={projects} title="All Projects" showLink />
            <Blogs blogs={blogs} title="Latest Blogs" showLink />
        </Layout>
    )
}
export const query = graphql`
    {
        allStrapiProjects(filter: { featured: { eq: true } }) {
            nodes {
                github
                id
                description
                title
                url
                image {
                    childImageSharp {
                        fluid {
                            src
                            ...GatsbyImageSharpFluid
                        }
                    }
                }
                stack {
                    id
                    title
                }
            }
        }
        allStrapiBlogs(
            filter: {}
            sort: { fields: date, order: DESC }
            limit: 3
        ) {
            nodes {
                slug
                content
                desc
                date(formatString: "MMM Do, yyyy")
                id
                title
                category
                image {
                    childImageSharp {
                        fluid {
                            ...GatsbyImageSharpFluid
                        }
                    }
                }
            }
        }
    }
`
