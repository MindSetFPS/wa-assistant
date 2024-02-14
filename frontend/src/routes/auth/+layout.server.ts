console.log("hit routes/+layout.server.ts")

export const load = async ({ locals: { getSession } }) => {
    return {
      session: await getSession(),
    }
  }