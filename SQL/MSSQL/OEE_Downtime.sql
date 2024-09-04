CREATE TABLE [dbo].[OEE_Downtime] (
    [DowntimeId]    UNIQUEIDENTIFIER NOT NULL,
    [BeginDateTime] DATETIME         NOT NULL,
    [EndDateTime]   DATETIME         NULL,
    [ContextId]     UNIQUEIDENTIFIER NULL,
    [EventDateTime] DATETIME         NULL,
    [Category]      VARCHAR (50)     NULL,
    [Reason]        VARCHAR (50)     NULL,
    [Planned]       BIT              NULL,
    CONSTRAINT [PK_OEE_Downtime] PRIMARY KEY NONCLUSTERED ([DowntimeId] ASC)
);


GO
CREATE NONCLUSTERED INDEX [IX_OEE_Downtime_ContextId]
    ON [dbo].[OEE_Downtime]([ContextId] ASC);


GO
CREATE CLUSTERED INDEX [IX_OEE_Downtime_BeginDateTime]
    ON [dbo].[OEE_Downtime]([BeginDateTime] ASC);

