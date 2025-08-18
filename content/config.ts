import { z, defineCollection } from "astro:content";

const projectCollection = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    article: z.string().url().optional(),
    repo: z.string().url().optional(),
    year: z.number(),
  }),
});

export const collections = {
  projects: projectCollection,
};
